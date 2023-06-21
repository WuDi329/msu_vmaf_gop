import numpy as np
import re
import matplotlib.pyplot as plt
import os
from datetime import datetime

def read_vmaf(vmaf_path): 
    all_scores = []
    with open(vmaf_path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            elements = line.split(' ')
            time_str = elements[3]
            time_obj = datetime.strptime(time_str, '%M:%S.%f')
            time_float = time_obj.minute * 60 + time_obj.second + time_obj.microsecond / 1000000
            all_scores.append(time_float)
    # print(all_scores)
    return all_scores

def read_vmaf_gops(vmaf_path):
    all_scores = []
    with open(vmaf_path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            elemets = line.split(' ')
            print(elemets)
            all_scores.append(float(elemets[7]))
    # print(all_scores)
    return all_scores

def read_path(path):
    all_paths = []
    with open(path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            elements = line.split(' ')
            all_paths.append(elements[-1])
    return all_paths

pred = read_vmaf_gops('/home/wudi/desktop/vmaf_gop_test/crf_vmaf_gop/crf-19.txt')
print(pred)

real = read_vmaf('/home/wudi/desktop/vmaf_gop_test/crf_vmaf_subsample40_threads/crf-19.txt')
print(real)

paths = read_path('/home/wudi/desktop/vmaf_gop_test/crf_vmaf_subsample40_threads/crf-19.txt')
print(paths)

x_labels = [path.split('_')[0] for path in paths]

x = np.arange(len(paths))
width = 0.35

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, pred, width, label='split vmaf time')
rects2 = ax.bar(x + width/2, real, width, label='Real vmaf time')

ax.set_ylabel('Time Cost (s)')
ax.set_title('VMAF time cost for CRF-19')
ax.set_xticks(x)
ax.set_xticklabels(x_labels , rotation=90)
ax.legend()

fig.tight_layout()

plt.savefig('time.png')
plt.close()