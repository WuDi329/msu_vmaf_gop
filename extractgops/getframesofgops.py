import subprocess
import os
# 这个模块的代码是为了将每个视频的Gop的帧数写入到文件中
# 视频文件路径
video_path = "/dataset/dataset/reference_videos/"
time_path = "/home/wudi/desktop/dataset_operation/I-numbers-all/"
output_path = "/home/wudi/desktop/dataset_operation/Numberofframes/"


for path in sorted(os.listdir(video_path)):
    if not path.endswith(".mp4"):
        continue
    # 调用mediainfo命令行工具获取时长
    output = subprocess.check_output(["mediainfo", "--Inform=Video;%Duration%", video_path+path])
    # 调用mediainfo命令行工具获取视频的帧率
    rate = subprocess.check_output(["mediainfo", "--Inform=Video;%FrameRate%", video_path+path])
    rate = float(rate.strip())
    print(rate)
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
    frames = [int(round(d * rate)) for d in duration ]
    print(f"{path} lines is", timestamps)
    print(f"{path} duration is", duration)
    print(f"{path} frames is", frames)

    frames_path = os.path.join(output_path, timestamp_file)
    # 这里将每一个帧的数量输入到文件中
    with open(frames_path, "w") as f:
        for frame in frames:
            f.write(str(frame) + "\n")
        # 打印结果
    print(f"{path} frames are written to file:", frames_path)
    # 打印时长
    # print(f"{path} length is ", video_length)