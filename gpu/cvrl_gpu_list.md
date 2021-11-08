# CVRL GPU Node List

The header/gpu type queue names are not up-to-date

@cvrl_titanx
    qa-titanx-013
    qa-titanx-014
@cvrl_1080ti
    qa-1080ti-015
    qa-1080ti-016
@cvrl_xp
    qa-xp-014
    qa-xp-013
    qa-xp-012
@cvrl_rtx6k
    qa-rtx6k-043
    qa-rtx6k-044
    qa-rtx6k-048
@czajka
    qa-rtx6k-017

## Blacklist on one line

This may only work with `qsub`.
Errors occur in use with `qrsh`.

```
#$ -l -h=!qa-titanx-013&!qa-titanx-014&!qa-1080ti-015&!qa-1080ti-016&!qa-xp-014&!qa-xp-013&!qa-xp-012&!qa-rtx6k-043&!qa-rtx6k-044&!qa-rtx6k-048&!qa-rtx6k-017
```
