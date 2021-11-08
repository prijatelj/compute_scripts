#!/bin/bash

# This bash script simply echoes the CRC environment variables for saving at
# the beginning of every crc job log. It is recommended to run this script at
# the beginning of every CRC job script for debugging purposes. It may also
# help to run this before and after setting up your environment to observe
# correct changes.

echo "Profile CRC Environment Variables:"
echo "  NOTE: These Environment Variables may not always be set, and whether or not that is okay depends on the specific situation."
echo ""
echo "  date                    = $(date +"%Y-%m-%d %T")"
echo ""
echo "  HOSTNAME                = $HOSTNAME"
echo "  ARC                     = $ARC"
echo "  COMMD_PORT              = $COMMD_PORT"
echo "  HOME                    = $HOME"
echo "  HOSTNAME                = $HOSTNAME"

echo ""
echo "Job Environment Variables:"
echo "  JOB_ID                  = $JOB_ID"
echo "  JOB_NAME                = $JOB_NAME"
echo "  LOGNAME                 = $LOGNAME"
echo "  NHOSTS                  = $NHOSTS"
echo "  NQUEUES                 = $NQUEUES"
echo "  NSLOTS                  = $NSLOTS"

echo ""
echo "SGE Job Environment Variables:"
echo "  SGE_CELL                = $SGE_CELL"
echo "  SGE_CKPT_ENV            = $SGE_CKPT_ENV"
echo "  SGE_CKPT_DIR            = $SGE_CKPT_DIR"
echo "  SGE_CLUSTER_NAME        = $SGE_CLUSTER_NAME"
echo "  SGE_JOB_SPOOL_DIR       = $SGE_JOB_SPOOL_DIR"

echo ""
echo "SGE Job Owner Environment Variables:"
echo "  SGE_O_HOME              = $SGE_O_HOME"
echo "  SGE_O_HOST              = $SGE_O_HOST"
echo "  SGE_O_LOGNAME           = $SGE_O_LOGNAME"
echo "  SGE_O_MAIL              = $SGE_O_MAIL"
echo "  SGE_O_PATH              = $SGE_O_PATH"
echo "  SGE_O_SHELL             = $SGE_O_SHELL"
echo "  SGE_O_TZ                = $SGE_O_TZ"
echo "  SGE_O_WORKDIR           = $SGE_O_WORKDIR"

echo ""
echo "SGE Job Root and Path Environment Variables:"
echo "  SGE_ROOT                = $SGE_ROOT"
echo "  SGE_STDERR_PATH         = $SGE_STDERR_PATH"
echo "  SGE_STDOUT_PATH         = $SGE_STDOUT_PATH"

echo ""
echo "Task Array Environment Variables:"
echo "  SGE_TASK_ID             = $SGE_TASK_ID"
echo "  SGE_TASK_FIRST          = $SGE_TASK_FIRST"
echo "  SGE_TASK_LAST           = $SGE_TASK_LAST"
echo "  SGE_TASK_STEPSIZE       = $SGE_TASK_STEPSIZE"

echo ""
echo "GPU Node Environment Variables:"
echo "  SGE_GPU                 = $SGE_GPU"
echo "  SGE_HGR_gpu_card        = $SGE_HGR_gpu_card"
echo "  CUDA_VISIBLE_DEVICES    = $CUDA_VISIBLE_DEVICES"

echo ""
echo "Nvidia Details:"
nvidia-smi

echo ""
echo "General Environment Variables:"
echo "  USER                    = $USER"
echo "  PWD                     = $PWD"
echo "  SHELL                   = $SHELL"
echo "  PATH                    = $PATH"

echo ""
echo "Python Details:"
echo "  python --version"
python --version
echo "  which python"
which python
echo "  PYTHONPATH              = $PYTHONPATH"

echo""
echo "Host's Active Jobs"
echo "qstat -l h=$HOSTNAME"
qstat -l h=$HOSTNAME
