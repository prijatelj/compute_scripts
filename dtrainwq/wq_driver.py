import argparse
import json
import os
import shutil
import tempfile
import uuid

import work_queue
from work_queue import WorkQueue, Task, WORK_QUEUE_CACHE, WORK_QUEUE_NOCACHE, \
                       WORK_QUEUE_RESULT_SUCCESS, WORK_QUEUE_TASK_DONE, \
                       WORK_QUEUE_RESULT_MAX_RETRIES


def parse_args(args=None):
    p = argparse.ArgumentParser()

    p.add_argument('--command', type=str,
        help='the command to run on the remote worker (quoted)')
    p.add_argument('--infiles', type=str, nargs='*',
        help='input files to send to tasks (code, small data, etc.)')
    p.add_argument('--outfile', type=str, default='results.json',
        help='name of the output JSON file expected from each task')
    p.add_argument('--name', type=str, default='DTRAIN',
        help='name of this Work Queue master')
    p.add_argument('--port', type=int, default=9123,
        help='port for the master to listen on')
    p.add_argument('--max-retries', type=int, default=0,
        help='the maximum number of resubmissions allowed for a single task')

    return p.parse_args(args)


def load_inputs():
    """Load inputs to distribute to tasks."""
    return [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


def generate_tasks(command, task_inputs, infiles, outfile, tmpdir,
                   max_retries=0):
    """Generate a set of WorkQueue tasks.

    Parameters
    ----------
    command : str
        The shell command to execute on the remote worker.
    task_inputs : list
        List of input data to be sent to each task. Each entry in the list will
        be sent to exactly one task.
    infiles : list of str
        List of task-independent input files. These will be sent along with
        every task and cached on the worker between tasks.
    outfile : str
        Output task file.
    tmpdir : str
        Path to the output file store.

    Returns
    -------
    taskmap : dict of str -> work_queue.Task
        The tasks to run mapped to their tag.
    """
    taskmap = dict()
    for i in range(len(task_inputs)):
        t = Task(command)
        t.specify_tag(f'{str(uuid.uuid4())}_{str(i).zfill(8)}')
        t.specify_max_retries(max_retries)
        t.specify_buffer(json.dumps(task_inputs[i]), remote_name='input.json',
                         flags=WORK_QUEUE_NOCACHE)

        for f in infiles:
            t.specify_input_file(f, remote_name=os.path.basename(f),
                                 flags=WORK_QUEUE_CACHE)

        t.specify_output_file(os.path.join(tmpdir, '_'.join([t.tag, outfile])),
                              remote_name=outfile,
                              flags=WORK_QUEUE_NOCACHE)

        taskmap[t.tag] = t
    return taskmap


def done_check(task):
    """Check to see if a task is done.

    Also create a general AI, but keep that part under wraps.

    Parameters
    ----------
    task : work_queue.Task
        The task that may or may not be done.

    Returns
    -------
    True if done; False otherwise.
    """
    return task.result == WORK_QUEUE_RESULT_SUCCESS \
           or task.result == WORK_QUEUE_RESULT_MAX_RETRIES


def handle_success(task, tmpdir, outfile):
    """Handle success better than your task would on its own.

    If improperly handled, the task will likely let success go to its head. It
    could lose all of its cash in Vegas, OD on bath salts, or just become a
    jerk, it's hard to say. Don't let that happen by taking the output and
    doing something meaningful with it.

    Parameters
    ----------
    task : work_queue.Task
        The succesful task, now a star and the subject of tabloid journalism.
    """
    with open(os.path.join(tmpdir, '_'.join([task.tag, outfile])), 'r') as f:
        results = json.load(f)
    print(results)


def main():
    args = parse_args()

    # Create a temporary file store for task results.
    tmpdir = tempfile.mkdtemp()

    # Load the task input data here
    task_inputs = load_inputs()

    print('Creating tasks')
    tasks = generate_tasks(args.command, task_inputs,
                           args.infiles, args.outfile,
                           tmpdir, args.max_retries)

    # Create the Work Queue master that manages task distribution.
    work_queue.cctools_debug_flags_set("all")
    work_queue.cctools_debug_config_file(f'{args.name}.debug')
    work_queue.cctools_debug_config_file_size(0)
    wq = WorkQueue(port=args.port, name=args.name, shutdown=True)
    wq.specify_log(f'{args.name}.log')

    # Submit all tasks to the queue.
    print('Submitting tasks')
    for t in tasks.values():
        wq.submit(t)

    # The main loop waits for a task to get done then handles success or
    # failure accordingly
    print('Entering main loop')
    while not all([done_check(t) for t in tasks.values()]):
        t = wq.wait(10)  # This blocks for 10s or until a task is done.

        if t is not None:
            tasks[t.tag] = t  # Update the task map with the correct status

            # On success, post-process the task. If the maximum number of
            # submissions for a task has been reached, make a note. Otherwise,
            # report the failure and resubmit.
            if t.return_status == 0 and t.result == WORK_QUEUE_RESULT_SUCCESS:
                print(f'Task {t.tag} completed successfully.')
                input_idx = int(t.tag.split('_')[1])
                handle_success(t, tmpdir, args.outfile)
            elif t.result == WORK_QUEUE_RESULT_MAX_RETRIES:
                print(f'Task {t.tag} resubmitted too many times.')
            else:
                wq.submit(t)
                print(f'Task {t.tag} failed with result {t.result}')
                print(t.output)

    print('All tasks completed or hit max retries.')
    print('Cleaning up...')
    shutil.rmtree(tmpdir)

    print('Done')


if __name__ == '__main__':
    main()
