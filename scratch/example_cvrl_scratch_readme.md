# Scratch 22 usage: dprijate
2020-06-24: dprijate and jhuang24 advised by Walter Scheirer are using this for the DARPA funded Open Set Recognition projects. Specifically for storing task datasets and results.

## Check Disk Space / File Storage
For AFS systems, such as the cvrl scratch directories, you may use the following command to recieve the total usage of the volume:
```
fs quota /afs/crc.nd.edu/group/cvrl/scratch_22/
```

Use the following command to recursively calculate the total amount of disk space usage of a directory's contents:
```
du -hc /afs/crc.nd.edu/group/cvrl/scratch_22/dprijate
```
You may want to run that as a job to the crc queue, if it takes a long time complete.
The `fs quota` command runs very fast in comparison, but only calculates the volume usage, not specific directory usage.
