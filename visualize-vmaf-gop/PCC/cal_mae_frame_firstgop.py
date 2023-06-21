from scipy import stats
import os
import numpy as np
import re
import csv
import linecache
from sklearn.metrics import mean_absolute_error

ref_path="/home/wudi/desktop/dataset_operation/visualize-vmaf-gop/logfile_score_firstgop/"
true_path="/home/wudi/desktop/dataset_operation/vmaf/logfile_score/"

def read_vmaf(sample_path, all_path): 
    pred_scores = []
    true_scores = []
    seq = []
    with open(sample_path, 'r') as f:
        reader = csv.reader(f, delimiter=' ')
        for row in reader:
            seq.append(int(row[0].split('"')[1]))
            pred_scores.append(float(row[1].split('"')[1]))
    # print(seq)
    # print(all_path)
    for i in range(len(seq)):
        # print(i)
        true_scores.append(float((linecache.getline(all_path, seq[i]+1)).split('"')[1]))
    # print(pred_scores)
    # print(true_scores)
    return pred_scores, true_scores

# 循环对所有文件进行处理
for path in os.listdir(ref_path):
    true_scores = []
    pred_scores = []
    # path = path.strip()
    # paths.append(path)
    pred_scores, true_scores = read_vmaf(ref_path + path, true_path + path)
    # print('pred_scores', pred_scores)
    # print('true_scores', true_scores)
    mae = mean_absolute_error(pred_scores, true_scores)
    print('当前', path, '的mae是', mae)

# pred_scores, true_scores = read_vmaf(ref_path + 'basketball_10sec_1920x1080_24.txt', true_path + 'basketball_10sec_1920x1080_24.txt')
# mae = mean_absolute_error(pred_scores, true_scores)
# print(mae)
