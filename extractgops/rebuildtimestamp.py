import os
import subprocess
video_path = "/dataset/dataset/reference_videos/"
time_path = "/home/wudi/desktop/vmaf_gop_test/I-numbers-all/"

for path in sorted(os.listdir(video_path)):
    if not path.endswith(".mp4"):
        continue
    # 调用mediainfo命令行工具获取时长
    output = subprocess.check_output(["mediainfo", "--Inform=Video;%Duration%", video_path+path])
    video_length = float(output.strip())/1000

    # 生成时间戳文件名
    timestamp_file = os.path.splitext(path)[0].replace(".mp4", "") + ".txt"
    timestamp_path = os.path.join(time_path, timestamp_file)

    timestamps = []
    # 将时间戳写入文件
    with open(timestamp_path, "r") as f:
        lines = f.readline().strip().split()
        timestamps = [x for x in lines]
    timestamps.append(f"{video_length:.3f}")
    print(timestamps)

    # duration = [round(j - i, 3) for i, j in zip(timestamps[:-1], timestamps[1:])]
    # # print(f"{path} duration ", duration)
    # frameofduration = [round(round(d * rate)/2) for d in duration]
    # middle = [round(t + (d/rate), 3) for t, d in zip(timestamps[:-1], frameofduration)]
    # middle_str = [f"{x:06.3f}" for x in middle]
    output_str = " ".join(timestamps)

    with open(timestamp_path, "w") as f:
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