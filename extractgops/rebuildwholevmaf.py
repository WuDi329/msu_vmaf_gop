# 这个模块的作用是将提取的gops的vmaf分数重新计算，得到真实的vmaf分数
# 第五步：重新构建真实vmaf分数
import subprocess
import os
import re

# 视频文件路径
data_path= "/home/wudi/desktop/dataset_operation/vmaf&numbers_middle/"
output_path = "/home/wudi/desktop/dataset_operation/vmaf/"

def read_vmaf(vmaf_path): 
    all_scores = []
    numbers = []
    with open(vmaf_path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith('vmaf='):
                m = re.search(r'\d+(\.\d+)?', line)
                vmaf = float(m.group(0))
                all_scores.append(vmaf)
                numbers.append(int(line.strip().split()[1]))
    # print(all_scores)
    # print(numbers)
    return all_scores, numbers

def calculate_final_vmaf(scores, numbers):
    # 计算分数加权平均值
    weighted_sum = 0
    total_weight = sum(numbers)
    for score, weight in zip(scores, numbers):
        weighted_sum += score * weight
    weighted_average = round(weighted_sum / total_weight, 6)
    return str(weighted_average)


files = []
final_scores = []
for path in sorted(os.listdir(data_path)):
    filename = path.replace(".txt", ".mp4")
    wholepath = os.path.join(data_path, path)
    scores, numbers = read_vmaf(wholepath)
    final_scores.append(calculate_final_vmaf(scores, numbers))
    files.append(filename)
    
# 这里将所有的文件的vmaf分数写入到最终文件中
output_path = os.path.join(output_path, "vmaf_result_16000k_gops_middle.txt")
with open(output_path, "w") as f:
    for score, filename in zip(final_scores, files):
        f.write(f"{score.ljust(10, '0')}   {filename}\n")
    
    
    # with open(wholepath, "r") as f:
    #     lines = f.readline().strip().split()
    #     timestamps = [float(x) for x in lines]

    # # 调用mediainfo命令行工具获取帧率
    # output = subprocess.check_output(["mediainfo", "--Inform=Video;%Duration%", video_path+path])
    # # 调用mediainfo命令行工具获取视频的帧率
    # rate = subprocess.check_output(["mediainfo", "--Inform=Video;%FrameRate%", video_path+path])
    # rate = float(rate.strip())
    # print(rate)
    # # 将输出转换为浮点数
    # video_length = float(output.strip())/1000

    # # 生成时间戳文件名
    # timestamp_file = os.path.splitext(path)[0].replace(".mp4", "") + ".txt"
    # timestamp_path = os.path.join(time_path, timestamp_file)

    # timestamps = []
    # # 将时间戳写入文件
    # with open(timestamp_path, "r") as f:
    #     lines = f.readline().strip().split()
    #     timestamps = [float(x) for x in lines]
    # timestamps.append(video_length)
    # duration = [round(j - i, 3) for i, j in zip(timestamps[:-1], timestamps[1:])]
    # frames = [int(round(d * rate)) for d in duration ]
    # print(f"{path} lines is", timestamps)
    # print(f"{path} duration is", duration)
    # print(f"{path} frames is", frames)

    # frames_path = os.path.join(output_path, timestamp_file)
    # with open(frames_path, "w") as f:
    #     for frame in frames:
    #         f.write(str(frame) + "\n")
    #     # 打印结果
    # print(f"{path} frames are written to file:", frames_path)
    # 打印时长
    # print(f"{path} length is ", video_length)