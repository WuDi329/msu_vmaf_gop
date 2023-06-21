import numpy as np
import re
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import os
from datetime import datetime

def read_vmaf(vmaf_path): 
    all_scores = []
    with open(vmaf_path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            elements = line.split(' ')
            print(elements)
            time_str = elements[4]

            all_scores.append(float(time_str))
    # print(all_scores)
    return all_scores

def read_vmaf_gops(vmaf_path):
    all_scores = []
    with open(vmaf_path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            elemets = line.split(' ')
            # print(elemets)
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

# def read_vmaf_clock(vmaf_path): 
#     all_scores = []
#     with open(vmaf_path, 'r') as f:
#         lines = f.readlines()
#         for line in lines:
#             elements = line.split(' ')
#             time_str = elements[3]
#             time_obj = datetime.strptime(time_str, '%M:%S.%f')
#             time_float = time_obj.minute * 60 + time_obj.second + time_obj.microsecond / 1000000
#             all_scores.append(time_float)
#     # print(all_scores)
#     return all_scores

pred = read_vmaf_gops('/home/wudi/desktop/vmaf_gop_test/crf_vmaf_gop_avg/crf-19.txt')
print(pred)

base = read_vmaf('/home/wudi/desktop/vmaf_gop_test/crf_vmaf_threads_avg/19.txt')
print(base)

control2 = read_vmaf('/home/wudi/desktop/vmaf_gop_test/crf_vmaf_subsample40_threads_avg/crf-19.txt')
print(control2)

paths = read_path('/home/wudi/desktop/vmaf_gop_test/crf_vmaf_subsample40_threads/crf-19.txt')
print(paths)

control1 = read_vmaf('/home/wudi/desktop/vmaf_gop_test/crf_vmaf_subsample40_avg/crf-19.txt')

control3 = read_vmaf('/home/wudi/desktop/vmaf_gop_test/crf_vmaf_avg/19.txt')

x_labels = [path.split('_')[0] for path in paths]

x = np.arange(0, len(paths)*4, 4)
width = 1

fig, ax = plt.subplots()
ax.plot(x, base, label='base vmaf time')
ax.plot(x, pred, label='split vmaf time')
ax.plot(x, control2, label='control 2 vmaf time')
ax.plot(x, control1, label='control 1 vmaf time')
ax.plot(x, control3, label='control 3 vmaf time')


ax.set_ylabel('Time Cost (s)')
ax.set_title('VMAF time cost for CRF-19')
ax.set_xticks(x)
ax.set_xticklabels(x_labels , rotation=90)
ax.legend()

ax.margins(x=0.1)

fig.tight_layout()

plt.savefig('time.png')
plt.close()



fig, axs = plt.subplots(2, 2, figsize=(10, 8))

axs[0, 0].plot(x, base, label='base vmaf time')
axs[0, 0].set_title('Base VMAF Time')
axs[0, 0].set_xticks(x)
axs[0, 0].set_xticklabels(x_labels, rotation=90)
axs[0, 0].legend()

axs[0, 1].plot(x, pred, label='split vmaf time')
axs[0, 1].set_title('Split VMAF Time')
axs[0, 1].set_xticks(x)
axs[0, 1].set_xticklabels(x_labels, rotation=90)
axs[0, 1].legend()

axs[1, 0].plot(x, control2, label='control 2 vmaf time')
axs[1, 0].set_title('Control 2 VMAF Time')
axs[1, 0].set_xticks(x)
axs[1, 0].set_xticklabels(x_labels, rotation=90)
axs[1, 0].legend()

axs[1, 1].plot(x, control1, label='control 1 vmaf time')
axs[1, 1].set_title('Control 1 VMAF Time')
axs[1, 1].set_xticks(x)
axs[1, 1].set_xticklabels(x_labels, rotation=90)
axs[1, 1].legend()

fig.tight_layout()
plt.savefig('time2.png')
plt.close()

# 绘制柱状图
plt.bar(x, base)

# 设置图表标题和坐标轴标签
plt.title('Base VMAF Time')
plt.xlabel('CRF')
plt.ylabel('Time Cost (s)')

# 设置x轴刻度标签
plt.xticks(x, x_labels, rotation=90)

# 显示图表
# plt.show()

plt.savefig('time3.png')
plt.close()