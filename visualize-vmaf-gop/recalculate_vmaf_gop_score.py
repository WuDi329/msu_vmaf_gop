import os
import numpy as np
import csv

# 作用是将清洗过的数据重新处理，获得gop中的各个帧的vmaf的平均值

ref_path="/home/wudi/desktop/dataset_operation/visualize-vmaf-gop/logfile_score_firstgop/"


def read_vmaf(sample_path): 
    pred_scores = []
    with open(sample_path, 'r') as f:
        reader = csv.reader(f, delimiter=' ')
        for row in reader:
            pred_scores.append(float(row[1].split('"')[1]))
    # print(seq)
    # print(pred_scores)
    # print(true_scores)
    return pred_scores

# 循环对所有文件进行处理
with open('/home/wudi/desktop/dataset_operation/visualize-vmaf-gop/regenerate_gop_score.txt', 'w') as f:
    for path in sorted(os.listdir(ref_path)):
        true_scores = []
        pred_scores = []
        # path = path.strip()
        # paths.append(path)
        pred_scores = read_vmaf(ref_path + path)
        average = np.mean(pred_scores)
        average = f"{average:.6f}"
        # mae = mean_absolute_error(pred_scores, true_scores)
        print(path, average)
        f.write(str(average) + '\n')
f.close()

# pred_scores, true_scores = read_vmaf(ref_path + 'basketball_10sec_1920x1080_24.txt', true_path + 'basketball_10sec_1920x1080_24.txt')
# mae = mean_absolute_error(pred_scores, true_scores)
# print(mae)
