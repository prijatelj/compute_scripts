# CRC CVRL GPU Usage
There is no real documentation on how to use the lab's CRC GPUs queues and how to use them without causing problems to others.
I am storing all of that information here.

## Xymon Monitor usage of CRC
This requires to be on the Notre Dame VPN or network at least.

mon.crc.nd.edu

## Available Gpus
`gpu@@cvrl_gpu`

For when needing a more specific gpu specify one of the following, such as needing 12GB of VRAM, use titanxp machine.

All others than 11

- `gpu@@cvrl-titanx`
    - 12Gb VRAM ( ? says Sam)
    - sam says it is a little bit slower.
- `gpu@@cvrl-1080ti`
    - 11Gb VRAM
- `cpu@@cvrl-titanxp`
    - possibly this one is wrong in its name?
        - possibly `cpu@@cvrl-xp`
    - 12Gb VRAM
    - these are the "best", out of the set.
- `gpu@@cvrl_rtx6k`
    - 24 GB Ram
    - 2 nodes, 4 GPUs each

Sam says we have access to titanxp # 13 and 14.

### Other Queues

Putting other non-gpu queues here for future reference.
These go under `#$ -q queue_name`

- 'debug'
    + 24 cores, 64GB of RAM. 1 hour only, no limit on cores. normal priority.
    + public
- 'long@@cvrl' or 'long@@cvrl_cpu'
    + for CPU machines for CVRL use only.

Checking nodes in use: `nodesInUse.sh queue`.
Checking free nodes: `free_nodes.sh queue`


## Example usage
`qsub -q gpu@@cvrl_gpu -pe smp 4 -l gpu_card=1 myjob.job`

The command line args can be put at the top of the jobscript in the usual way.

`gpu_card=1` means to request access to one gpu only.
So this is the number of gpus being requested at a time for a job.

### Interactive Example
`qrsh -q gpu@cvrl -l gpu=1 -pe smp 1`
When doing interactive jobs, to not interfere with other's jobs use:

`export CUDA_VISIBLE_DEVICES=${SGE_HGR_gpu_card// /,}`

## Check usage
Able to check who is currently using any of these nodes with:
`nodesInUse.sh @cvrl_gpu`

## Jeff Kinnison Notes:
Historically, if you're using 1 GPU you request 1/4 of the cores on the machine, 2 GPUs -> 1/2 of the cores, and so on up to 4 GPUs
`gpu_card` is how you specify the number of GPUs.

## CVRL CPU only machines
For cpu only machines under cvrl: `long@@cvrl_cpu`

## Submit job to specific machine
`-q long -l hostname=d12chas332` to get the exact host machine d12chas332 in the long queue.

## Tensorflow and python
To use tensorflow on the CRC do not use the tensorflow module, but instead use `module add conda` to use the CRC conda, and install tensorflow and all python packages this way.
This allows the most flexibility in using python on the CRC giving the user full control over their python environment via conda.
Install tensorflow-gpu for the gpu, etc...

## When things are missing in modules
If anything is required to run on the CRC but not included in modules and the CRC maintainers are unable to provide the module, then one can try to use "singularity" to make containers.

## Interactive CRC session
Typically, `qsub` is used to submit jobs to CRC to be computed, but sometimes, esp. during debugging, we may want to work on a CRC worker machine.
To do so, use `qrsh` with the desired commands as typicaly for qsub to request an interactive session.
If a machine is available, you will be logged into that machine in an interactive session and may work as necessary.
However, this interactive session is unable to be turned into a job to be run, you still must submit such jobs via `qsub`.
