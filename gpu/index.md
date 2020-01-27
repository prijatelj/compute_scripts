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

Sam says we have access to titanxp # 13 and 14.


## Example usage
`qsub -q gpu@@cvrl_gpu -pe smp 4 -l gpu_card=1 myjob.job`

The command line args can be put at the top of the jobscript in the usual way.

`gpu_card=1` means to request access to one gpu only.
So this is the number of gpus being requested at a time for a job.

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
