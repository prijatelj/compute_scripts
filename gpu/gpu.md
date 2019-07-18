#CRC CVRL GPU Usage
There is no real documentation on how to use the lab's CRC GPUs queues and how to use them without causing problems to others.
I am storing all of that information here.

##Xymon Monitor usage of CRC
This requires to be on the Notre Dame VPN or network at least.

mon.crc.nd.edu

##Available Gpus
`gpu@@cvrl_gpu`

For when needing a more specific gpu specify one of the following
, such as needing 12GB of VRAM, use titanxp machine.

- `gpu@@cvrl-titanx`
- `gpu@@cvrl-1080ti`
- `cpu@@cvrl-titanxp`
    - (possibly this one is wrong in its name?)


## Example usage
`qsub -q gpu@@cvrl_gpu -pe smp 4 -l gpu_card=1 myjob.job`

The command line args can be put at the top of the jobscript in the usual way.

## Jeff Kinnison Notes:
Historically, if you're using 1 GPU you request 1/4 of the cores on the machine, 2 GPUs -> 1/2 of the cores, and so on up to 4 GPUs
`gpu_card` is how you specify the number of GPUs.
