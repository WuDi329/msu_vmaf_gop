import numpy as np
import re
from scipy.stats import pearsonr
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

mae_list = []
variance_list = []
r_list = []
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

def getRelativeError(dist, real):
    return np.mean(np.abs((dist - real) / real))

def getVariance(dist, real):
    return np.var(np.abs((dist - real) / real))

def evaluate(dist, real, name):
    mean_error = getRelativeError(dist, real)
    variance = getVariance(dist, real)
    mae = np.mean(np.abs(dist - real))
    mae_list.append(mae)
    variance_list.append(variance)
    print(f"The relative error between real and {name} is {mean_error}.")
    print(f"The mean absolute error between real and {name} is {mae}.")
    print(f"The variance between real and {name} is {variance}.")
    


dist2 = read_vmaf('/home/wudi/desktop/dataset_operation/visualize-vmaf/data/vmaf_result_sample2.txt')
# print(dist1)
dist = read_vmaf('/home/wudi/desktop/dataset_operation/visualize-vmaf/data/vmaf_result_16000k.txt')
# print(dist2)
# Define the two distributions as numpy arrays
dist2 = np.array(dist2)
dist = np.array(dist)
r, p = pearsonr(dist2, dist)
print('sample2 vmaf 和 真实值的相关系数为', r)
print('sample2 vmaf 和 真实值的可能性为', p)
print('')
plt.xlim(80, 100)
plt.ylim(80, 100)
plt.xticks(range(80, 101, 5))
plt.yticks(range(80, 101, 5))
# Set the aspect ratio to 'equal' to ensure equal length of x and y axes
plt.gca().set_aspect('equal', adjustable='box')
plt.scatter(dist2, dist)
plt.xlabel('sample2-vmaf')
plt.ylabel('real-vmaf')
plt.savefig('/home/wudi/desktop/dataset_operation/visualize-vmaf/PCC/sample2-fig.png')
plt.close()

dist5 = read_vmaf('/home/wudi/desktop/dataset_operation/visualize-vmaf/data/vmaf_result_sample5.txt')
dist5 = np.array(dist5)
# print(dist3)
r, p = pearsonr(dist5, dist)
print('sample5 vmaf 和 真实值的相关系数为', r)
print('sample5 vmaf 和 真实值的可能性为', p)
print('')
plt.xlim(80, 100)
plt.ylim(80, 100)
plt.xticks(range(80, 101, 5))
plt.yticks(range(80, 101, 5))
# Set the aspect ratio to 'equal' to ensure equal length of x and y axes
plt.gca().set_aspect('equal', adjustable='box')
plt.scatter(dist5, dist)
plt.xlabel('sample5-vmaf')
plt.ylabel('real-vmaf')
plt.savefig('/home/wudi/desktop/dataset_operation/visualize-vmaf/PCC/sample5-fig.png')
plt.close()

dist10 = read_vmaf('/home/wudi/desktop/dataset_operation/visualize-vmaf/data/vmaf_result_sample10.txt')
dist10 = np.array(dist10)
# print(dist4)
r, p = pearsonr(dist10, dist)
print('sample10 vmaf 和 真实值的相关系数为', r)
print('sample10 vmaf 和 真实值的可能性为', p)
print('')
plt.xlim(80, 100)
plt.ylim(80, 100)
plt.xticks(range(80, 101, 5))
plt.yticks(range(80, 101, 5))
# Set the aspect ratio to 'equal' to ensure equal length of x and y axes
plt.gca().set_aspect('equal', adjustable='box')
plt.scatter(dist10, dist)
plt.xlabel('sample10-vmaf')
plt.ylabel('real-vmaf')
plt.savefig('/home/wudi/desktop/dataset_operation/visualize-vmaf/PCC/sample10-fig.png')
plt.close()

dist20 = read_vmaf('/home/wudi/desktop/dataset_operation/visualize-vmaf/data/vmaf_result_sample20.txt')
dist20 = np.array(dist20)
# print(dist5)
r, p = pearsonr(dist20, dist)
print('sample20 vmaf 和 真实值的相关系数为', r)
print('sample20 vmaf 和 真实值的可能性为', p)
r_list.append(r)
evaluate(dist20, dist, 'dist20')
print('')
plt.xlim(80, 100)
plt.ylim(80, 100)
plt.xticks(range(80, 101, 5))
plt.yticks(range(80, 101, 5))
# Set the aspect ratio to 'equal' to ensure equal length of x and y axes
plt.gca().set_aspect('equal', adjustable='box')
plt.scatter(dist20, dist)
plt.xlabel('sample20-vmaf')
plt.ylabel('real-vmaf')
plt.savefig('/home/wudi/desktop/dataset_operation/visualize-vmaf/PCC/sample20-fig.png')
plt.close()



dist30 = read_vmaf('/home/wudi/desktop/dataset_operation/visualize-vmaf/data/vmaf_result_sample30.txt')
dist30 = np.array(dist30)
r, p = pearsonr(dist30, dist)
print('sample30 vmaf 和 真实值的相关系数为', r)
print('sample30 vmaf 和 真实值的可能性为', p)
r_list.append(r)
evaluate(dist30, dist, 'dist30')
print('')
plt.xlim(80, 100)
plt.ylim(80, 100)
plt.xticks(range(80, 101, 5))
plt.yticks(range(80, 101, 5))
# Set the aspect ratio to 'equal' to ensure equal length of x and y axes
plt.gca().set_aspect('equal', adjustable='box')
plt.scatter(dist30, dist)
plt.xlabel('sample30-vmaf')
plt.ylabel('real-vmaf')
plt.savefig('/home/wudi/desktop/dataset_operation/visualize-vmaf/PCC/sample30-fig.png')
plt.close()



dist40 = read_vmaf('/home/wudi/desktop/dataset_operation/visualize-vmaf/data/vmaf_result_sample40.txt')
dist40 = np.array(dist40)
r, p = pearsonr(dist40, dist)
print('sample40 vmaf 和 真实值的相关系数为', r)
print('sample40 vmaf 和 真实值的可能性为', p)
r_list.append(r)
evaluate(dist40, dist, 'dist40')
print('')
plt.xlim(70, 100)
plt.ylim(70, 100)
plt.xticks(range(70, 101, 5))
plt.yticks(range(70, 101, 5))
# Set the aspect ratio to 'equal' to ensure equal length of x and y axes
plt.gca().set_aspect('equal', adjustable='box')
plt.scatter(dist40, dist)
plt.xlabel('sample40-vmaf')
plt.ylabel('real-vmaf')
plt.savefig('/home/wudi/desktop/dataset_operation/visualize-vmaf/PCC/sample40-fig.png')
plt.close()




dist50 = read_vmaf('/home/wudi/desktop/dataset_operation/visualize-vmaf/data/vmaf_result_sample50.txt')
dist50 = np.array(dist50)
r, p = pearsonr(dist50, dist)
print('sample50 vmaf 和 真实值的相关系数为', r)
print('sample50 vmaf 和 真实值的可能性为', p)
r_list.append(r)
evaluate(dist50, dist, 'dist50')
print('')
plt.xlim(80, 100)
plt.ylim(80, 100)
plt.xticks(range(80, 101, 5))
plt.yticks(range(80, 101, 5))
# Set the aspect ratio to 'equal' to ensure equal length of x and y axes
plt.gca().set_aspect('equal', adjustable='box')
plt.scatter(dist50, dist)
plt.xlabel('sample50-vmaf')
plt.ylabel('real-vmaf')
plt.savefig('/home/wudi/desktop/dataset_operation/visualize-vmaf/PCC/sample50-fig.png')
plt.close()


dist60 = read_vmaf('/home/wudi/desktop/dataset_operation/visualize-vmaf/data/vmaf_result_sample60.txt')
dist60 = np.array(dist60)
r, p = pearsonr(dist60, dist)
print('sample60 vmaf 和 真实值的相关系数为', r)
print('sample60 vmaf 和 真实值的可能性为', p)
r_list.append(r)
evaluate(dist60, dist, 'dist60')
print('')
plt.xlim(80, 100)
plt.ylim(80, 100)
plt.xticks(range(80, 101, 5))
plt.yticks(range(80, 101, 5))
# Set the aspect ratio to 'equal' to ensure equal length of x and y axes
plt.gca().set_aspect('equal', adjustable='box')
plt.scatter(dist60, dist)
plt.xlabel('sample60-vmaf')
plt.ylabel('real-vmaf')
plt.savefig('/home/wudi/desktop/dataset_operation/visualize-vmaf/PCC/sample60-fig.png')
plt.close()

dist70 = read_vmaf('/home/wudi/desktop/dataset_operation/visualize-vmaf/data/vmaf_result_sample70.txt')
dist70 = np.array(dist70)
r, p = pearsonr(dist70, dist)
print('sample70 vmaf 和 真实值的相关系数为', r)
print('sample70 vmaf 和 真实值的可能性为', p)
r_list.append(r)
evaluate(dist70, dist, 'dist70')
print('')
plt.xlim(80, 100)
plt.ylim(80, 100)
plt.xticks(range(80, 101, 5))
plt.yticks(range(80, 101, 5))
# Set the aspect ratio to 'equal' to ensure equal length of x and y axes
plt.gca().set_aspect('equal', adjustable='box')
plt.scatter(dist70, dist)
plt.xlabel('sample70-vmaf')
plt.ylabel('real-vmaf')
plt.savefig('/home/wudi/desktop/dataset_operation/visualize-vmaf/PCC/sample70-fig.png')
plt.close()



dist80 = read_vmaf('/home/wudi/desktop/dataset_operation/visualize-vmaf/data/vmaf_result_sample80.txt')
dist80 = np.array(dist80)
r, p = pearsonr(dist80, dist)
print('sample80 vmaf 和 真实值的相关系数为', r)
print('sample80 vmaf 和 真实值的可能性为', p)
r_list.append(r)
evaluate(dist80, dist, 'dist80')
print('')
plt.xlim(80, 100)
plt.ylim(80, 100)
plt.xticks(range(80, 101, 5))
plt.yticks(range(80, 101, 5))
# Set the aspect ratio to 'equal' to ensure equal length of x and y axes
plt.gca().set_aspect('equal', adjustable='box')
plt.scatter(dist80, dist)
plt.xlabel('sample80-vmaf')
plt.ylabel('real-vmaf')
plt.savefig('/home/wudi/desktop/dataset_operation/visualize-vmaf/PCC/sample80-fig.png')
plt.close()



dist90 = read_vmaf('/home/wudi/desktop/dataset_operation/visualize-vmaf/data/vmaf_result_sample90.txt')
dist90 = np.array(dist90)
r, p = pearsonr(dist90, dist)
print('sample90 vmaf 和 真实值的相关系数为', r)
print('sample90 vmaf 和 真实值的可能性为', p)
r_list.append(r)
evaluate(dist90, dist, 'dist90')
print('')
plt.xlim(80, 100)
plt.ylim(80, 100)
plt.xticks(range(80, 101, 5))
plt.yticks(range(80, 101, 5))
# Set the aspect ratio to 'equal' to ensure equal length of x and y axes
plt.gca().set_aspect('equal', adjustable='box')
plt.scatter(dist90, dist)
plt.xlabel('sample90-vmaf')
plt.ylabel('real-vmaf')
plt.savefig('/home/wudi/desktop/dataset_operation/visualize-vmaf/PCC/sample90-fig.png')
plt.close()



dist100 = read_vmaf('/home/wudi/desktop/dataset_operation/visualize-vmaf/data/vmaf_result_sample100.txt')
dist100 = np.array(dist100)
r, p = pearsonr(dist100, dist)
print('sample100 vmaf 和 真实值的相关系数为', r)
print('sample100 vmaf 和 真实值的可能性为', p)
r_list.append(r)
evaluate(dist100, dist, 'dist100')
print(dist100)
print(dist)
print('')
plt.xlim(80, 100)
plt.ylim(80, 100)
plt.xticks(range(80, 101, 5))
plt.yticks(range(80, 101, 5))
# Set the aspect ratio to 'equal' to ensure equal length of x and y axes
plt.gca().set_aspect('equal', adjustable='box')
plt.scatter(dist100[:36], dist[:36])
plt.xlabel('sample100-vmaf')
plt.ylabel('real-vmaf')
plt.savefig('/home/wudi/desktop/dataset_operation/visualize-vmaf/PCC/sample100-fig.png')
plt.close()




plt.plot([20, 30, 40, 50, 60, 70 , 80 , 90, 100], mae_list, label='MAE')
plt.plot([20, 30, 40, 50, 60, 70 , 80 , 90, 100], variance_list, label='Variance')
plt.plot([20, 30, 40, 50, 60, 70 , 80 , 90, 100], r_list, label='PCC')
plt.xlabel('dist')
plt.legend()
plt.savefig('/home/wudi/desktop/dataset_operation/visualize-vmaf/PCC/compare20-100.png')


# # 定义两组变量 dist5 和 dist2，假设它们之间有线性关系
# x = np.array([1, 2, 3, 4, 5])
# y = np.array([2, 4, 6, 8, 10])

# 创建一个线性回归模型
model = LinearRegression()

# 将 x 转换为 n×1 的二维数组
X = dist5[:, np.newaxis]

# 使用模型拟合数据
model.fit(X, dist2)

# 获取模型的斜率和截距
slope = model.coef_[0]
intercept = model.intercept_

# 输出函数关系
print(f"y = {slope}x + {intercept}")



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
