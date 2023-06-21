import os
import subprocess
# 这个模块的代码是为了获取每个视频每个GOP的中间的时间

video_path = "/dataset/dataset/reference_videos/"
time_path = "/home/wudi/desktop/dataset_operation/I-numbers-all/"
middle_path = "/home/wudi/desktop/dataset_operation/I-numbers-middle/"

for path in sorted(os.listdir(video_path)):
    if not path.endswith(".mp4"):
        continue
    # 调用mediainfo命令行工具获取时长
    output = subprocess.check_output(["mediainfo", "--Inform=Video;%Duration%", video_path+path])

    # 调用mediainfo命令行工具获取视频的帧率
    rate = subprocess.check_output(["mediainfo", "--Inform=Video;%FrameRate%", video_path+path])
    rate = float(rate.strip())
    # 将输出转换为浮点数
    video_length = float(output.strip())/1000

    # 生成时间戳文件名
    timestamp_file = os.path.splitext(path)[0].replace(".mp4", "") + ".txt"
    timestamp_path = os.path.join(time_path, timestamp_file)

    timestamps = []
    # 将时间戳写入文件
    with open(timestamp_path, "r") as f:
        lines = f.readline().strip().split()
        timestamps = [float(x) for x in lines]
    timestamps.append(video_length)

    duration = [round(j - i, 3) for i, j in zip(timestamps[:-1], timestamps[1:])]
    # print(f"{path} duration ", duration)
    frameofduration = [round(round(d * rate)/2) for d in duration]
    middle = [round(t + (d/rate), 3) for t, d in zip(timestamps[:-1], frameofduration)]
    middle_str = [f"{x:06.3f}" for x in middle]
    output_str = " ".join(middle_str)

    with open(os.path.join(middle_path, timestamp_file), "w") as f:
        f.write(output_str)



    # middle = []
    # for i in range(len(timestamps) - 1):
    #     average = round((timestamps[i] + timestamps[i+1]) / 2, 3)
    #     middle.append(average)
    # print(f"{path} timestamps ", timestamps)
    # print(f"{path} frame num ", frameofduration)
    print(f"{path} middle ", output_str)
    # 打印时长
    # print(f"{path} length is ", video_length)