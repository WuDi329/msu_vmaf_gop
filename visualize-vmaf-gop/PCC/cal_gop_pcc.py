import numpy as np
import re
from scipy.stats import pearsonr, spearmanr, kendalltau
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import os

def read_vmaf(vmaf_path): 
    all_scores = []
    with open(vmaf_path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            m = re.search(r'^\d+(\.\d+)?', line)
            if m:
                vmaf = float(m.group(0))
                all_scores.append(vmaf)
    # print(all_scores)
    return all_scores

def read_vmaf_gops(vmaf_path):
    all_scores = []
    with open(vmaf_path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            elemets = line.split(' ')
            all_scores.append(float(elemets[1]))
    # print(all_scores)
    return all_scores

def getRelativeError(dist, real):
    return np.mean(np.abs((dist - real) / real))

def getVariance(dist, real):
    return np.var(np.abs((dist - real) / real))

def evaluate(dist, real, name):
    mean_error = getRelativeError(dist, real)
    variance = getVariance(dist, real)
    mae = np.mean(np.abs(dist - real))
    print(f"The relative error between real and {name} is {mean_error}.")
    print(f"The mean absolute error between real and {name} is {mae}.")
    print(f"The variance between real and {name} is {variance}.")

r_list = []
mae = []
x_tag = []
for path in sorted(os.listdir('/home/wudi/desktop/vmaf_gop_test/crf_vmaf_threads/'), key=lambda x: int(x.split(".")[0])):
    ref_path = os.path.join('/home/wudi/desktop/vmaf_gop_test/crf_vmaf_threads_avg/', path)
    dis_path = os.path.join('/home/wudi/desktop/vmaf_gop_test/crf_vmaf_gop_avg/', "crf-"+path)
    dist_firstgop = read_vmaf_gops(dis_path)
    # print(dist1)
    dist = read_vmaf(ref_path)
    # print(dist2)
    # Define the two distributions as numpy arrays
    dist_firstgop = np.array(dist_firstgop)
    dist = np.array(dist)
    print(dist_firstgop)
    r, p = pearsonr(dist_firstgop, dist)
    average = np.mean(dist_firstgop)
    # if average >= 80:
    x_tag.append(path.split(".")[0])
    r_list.append(r)
    mae.append(np.mean(dist - dist_firstgop))
print(x_tag)




# # 创建一个新的图形
# fig, ax = plt.subplots()
# fig.set_size_inches(len(r_list)*0.5, 8)

# # 设置图形的标题和横纵坐标标签
# ax.set_title('Comparison of split and true vmaf value')
# ax.set_xlabel('Name')
# ax.set_ylabel('VMAF Score')

# # 设置横坐标的刻度和标签
# ax.set_xticks(np.arange(len(name_array)))
# ax.set_xticklabels(name_array, rotation=90)

# # 绘制pred_list和true_list的柱状图
# ax.bar(np.arange(len(name_array)) - 0.2, pred_array, width=0.4, label='split_vmaf_value')
# ax.bar(np.arange(len(name_array)) + 0.2, true_array, width=0.4, label='true_vmaf_value')

# # 添加图例
# ax.legend()

# fig.savefig('comparison.png')
# # 显示图形
# plt.close()


fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
fig.set_size_inches(len(r_list)*0.3, 8)

ax1.bar(range(len(r_list)), r_list, width=0.5)
ax1.set_xticks(range(len(x_tag)))
ax1.set_xticklabels(x_tag, rotation=45)
ax1.set_title('Pearson correlation coefficient')
ax1.set_ylabel('PCC')
ax1.set_xlabel('CRF')
for i, v in enumerate(r_list):
    ax1.text(i, v + 0.01, str(round(v, 2))[2:], ha='center')

ax2.bar(range(len(mae)), mae, width=0.5)
ax2.set_xticks(range(len(x_tag)))
ax2.set_xticklabels(x_tag, rotation=45)
ax2.set_title('Mean Absolute Error')
ax2.set_ylabel('MAE')
ax2.set_xlabel('CRF')
plt.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.9, hspace=0.5)
plt.savefig('/home/wudi/desktop/vmaf_gop_test/visualize-vmaf-gop/PCC/vmaf-gop-crf.png')
plt.close()

# plt.bar(range(len(r_list)), r_list, width= 0.5)
# plt.xticks(range(len(x_tag)), x_tag, rotation=45)
# plt.savefig('/home/wudi/desktop/vmaf_gop_test/visualize-vmaf-gop/PCC/vmaf-gop-crf-xcc.png')
# plt.close()
# print(mae)

# plt.bar(range(len(mae)), mae, width= 0.5)
# plt.xticks(range(len(x_tag)), x_tag, rotation=45)
# plt.savefig('/home/wudi/desktop/vmaf_gop_test/visualize-vmaf-gop/PCC/vmaf-gop-crf-relative-error.png')
# plt.close()



# plt.xlim(80, 100)
# plt.ylim(80, 100)
# plt.xticks(range(80, 101, 5))
# plt.yticks(range(80, 101, 5))
# # Set the aspect ratio to 'equal' to ensure equal length of x and y axes
# plt.gca().set_aspect('equal', adjustable='box')
# plt.scatter(dist_firstgop, dist)
# plt.xlabel('first-gop-vmaf')
# plt.ylabel('real-vmaf')
# plt.savefig('/home/wudi/desktop/vmaf_gop_test/visualize-vmaf-gop/PCC/firstgop-fig.png')
# plt.close()

# dist_gops = read_vmaf('/home/wudi/desktop/dataset_operation/visualize-vmaf-gop/data/vmaf_result_16000k_gops.txt')
# dist_gops = np.array(dist_gops)
# r, p = pearsonr(dist_gops, dist)
# print('gops 测量的vmaf 和 真实值的相关系数为', r)
# print('gops 测量的vmaf 和 真实值的可能性为', p)
# evaluate(dist_gops, dist, 'gops')
# plt.xlim(70, 100)
# plt.ylim(70, 100)
# plt.xticks(range(70, 101, 5))
# plt.yticks(range(70, 101, 5))
# # Set the aspect ratio to 'equal' to ensure equal length of x and y axes
# plt.gca().set_aspect('equal', adjustable='box')
# plt.scatter(dist_gops, dist)
# plt.xlabel('gops-vmaf')
# plt.ylabel('real-vmaf')
# plt.savefig('/home/wudi/desktop/dataset_operation/visualize-vmaf-gop/PCC/gops-fig.png')
# plt.close()

# dist_gops_middle = read_vmaf('/home/wudi/desktop/dataset_operation/visualize-vmaf-gop/data/vmaf_result_16000k_gops_middle.txt')
# dist_gops_middle = np.array(dist_gops_middle)
# r, p = pearsonr(dist_gops_middle, dist)
# print('gops middle 测量的vmaf 和 真实值的相关系数为', r)
# print('gops middle 测量的vmaf 和 真实值的可能性为', p)
# evaluate(dist_gops_middle, dist, 'middle ops')
# plt.xlim(70, 100)
# plt.ylim(70, 100)
# plt.xticks(range(70, 101, 5))
# plt.yticks(range(70, 101, 5))
# # Set the aspect ratio to 'equal' to ensure equal length of x and y axes
# plt.gca().set_aspect('equal', adjustable='box')
# plt.scatter(dist_gops_middle, dist)
# plt.xlabel('middle-gops-vmaf')
# plt.ylabel('real-vmaf')
# plt.savefig('/home/wudi/desktop/vmaf_gop_test/visualize-vmaf-gop/PCC/middle-gops-fig.png')
# plt.close()






# # 定义两组变量 dist5 和 dist2，假设它们之间有线性关系
# x = np.array([1, 2, 3, 4, 5])
# y = np.array([2, 4, 6, 8, 10])

# 创建一个线性回归模型
# model = LinearRegression()

# # 将 x 转换为 n×1 的二维数组
# X = dist_firstgop[:, np.newaxis]

# # 使用模型拟合数据
# model.fit(X, dist)

# # 获取模型的斜率和截距
# slope = model.coef_[0]
# intercept = model.intercept_

# # 输出函数关系
# print(f"y = {slope}x + {intercept}")



# # Calculate the mean of each distribution
# mean1 = np.mean(dist1)
# mean2 = np.mean(dist2)

# # Calculate the standard deviation of each distribution
# std1 = np.std(dist1)
# std2 = np.std(dist2)

# # Calculate the covariance between the two distributions
# covariance = np.cov(dist1, dist2)[0][1]

# # Calculate the Pearson Correlation Coefficient
# pcc = covariance / (std1 * std2)

# print(pcc)
