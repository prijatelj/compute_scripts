# Jeff's awk script that greedily gets the device number of the first unused
# GPU found in nvidia-smi output.
gpu=$(nvidia-smi -q -d PIDS | awk 'BEGIN { gpu = 0; n = 0; inc = 1; } /Attached/ { n += $4; } /Processes/ && NF < 3 { if (inc == 1) { gpu++; } } /Processes/ && NF == 3 { inc = 0; } END { if (gpu >= n) { print(-1) } if (gpu < n) { print gpu; } }')

# WARNING! if no devices are available, it will return -1, which crashes all CUDA code. Thus, make a check before assiging it to CUDA_VISIBLE_DEVICES.

export CUDA_VISIBLE_DEVICES=$gpu

# Putting these two commands in your job script above where you execute your
# GPU-using program will make it so that is the GPU you use.
