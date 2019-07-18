import os
import sys

if __name__ == '__main__':
    cuda = 'none'

    out = os.popen('nvidia-smi').read()
    if out != '':
        out = out.split('\n')

        for i, r in enumerate(out):
            if r == '                                                                               ':
                out = out[i + 5:-2]
                break

        indices = {0: True, 1: True, 2: True, 3: True}
        for r in out:
            try:  # this is to handle "no gpu processes"
                id_ = int(r.split()[1])
            except:
                break
            indices[id_] = False

        for i in indices:
            if indices[i]:
                cuda = i
                break
    print (cuda)
