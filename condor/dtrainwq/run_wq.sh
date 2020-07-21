#!/usr/bin/env bash

module load python/3.7.3
source ~/envs/shadho-env/bin/activate

export PATH="$PATH:$HOME/.shadho/bin"
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:$HOME/.shadho/lib"

wq_name='DTRAIN'
min_workers=10
max_workers=100

# Start up the Work Queue factory in the background
~/.shadho/bin/work_queue_factory \
    -M $wq_name \
    -T condor \
    -w $min_workers \
    -W $max_workers \
    --cores=1 \
    > log.out &

# Run the driver
python wq_driver.py \
    --command "bash test_task.sh" \
    --infiles "test_task.sh" \
    --name "$wq_name"

# Yes, this name is correct
pkill -9 work_queue_fact
