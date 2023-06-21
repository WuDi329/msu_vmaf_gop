import os
import subprocess
import time
import concurrent.futures
import re

# 第一步：根据I-numbers-middle抽取GOP（计时开始）
ref_path = "/dataset/dataset/reference_videos/"
gop_path= "/home/wudi/desktop/vmaf_gop_test/I-numbers-middle/"
time_path = "/home/wudi/desktop/vmaf_gop_test/I-numbers-all/"
files = [f for f in sorted(os.listdir(ref_path)) if os.path.isfile(os.path.join(ref_path, f))]
# 地址需要改
result_path = "/home/wudi/desktop/vmaf_gop_test/crf_vmaf_gop6/"
source_dir = ""
target_dir = ""
vmaf_dir = ""

# files是一个拥有两个元素的列表，它包含了相应的视频文件名
def run_vmaf(file):
    command = 'ffmpeg -i "{}" -i "{}" -lavfi "[0:v][1:v]libvmaf=psnr=1:n_threads=8:log_path={}.txt" -f null -'.format(os.path.join(target_dir, file), os.path.join(source_dir, file), os.path.join(vmaf_dir, file.split(".")[0]))
    print("当前执行指令：{}".format(command))
    subprocess.run(command, shell=True)

def get_frame_number(file):
    # 调用mediainfo命令行工具获取时长
    output = subprocess.check_output(["mediainfo", "--Inform=Video;%Duration%", os.path.join(ref_path, file)])
    # 调用mediainfo命令行工具获取视频的帧率
    rate = subprocess.check_output(["mediainfo", "--Inform=Video;%FrameRate%", os.path.join(ref_path, file)])
    rate = float(rate.strip())
    # 将输出转换为浮点数
    video_length = float(output.strip())/1000

    # 生成时间戳文件名
    timestamp_file = os.path.splitext(file)[0].replace(".mp4", "") + ".txt"
    timestamp_path = os.path.join(time_path, timestamp_file)

    timestamps = []
    # 将时间戳写入文件
    with open(timestamp_path, "r") as f:
        lines = f.readline().strip().split()
        timestamps = [float(x) for x in lines]
    timestamps.append(video_length)
    duration = [round(j - i, 3) for i, j in zip(timestamps[:-1], timestamps[1:])]
    frames = [int(round(d * rate)) for d in duration ]
    return frames

class Record():
    def __init__(self, filename, evaluate_vmaf, total_time, cut_time, evaluate_time, merge_time):
        self.filename = filename
        self.evaluate_vmaf = evaluate_vmaf
        self.total_time = total_time
        self.cut_time = cut_time
        self.evaluate_time = evaluate_time
        self.merge_time = merge_time

    def get_str(self):
        return "vmaf: {}    total time: {}    cut time: {}   evaluate_time: {}   merge_time: {}   {}\n".format(self.evaluate_vmaf, self.total_time, self.cut_time, self.evaluate_time, self.merge_time, self.filename)

def calculate_final_vmaf(scores, numbers):
    # 计算分数加权平均值
    weighted_sum = 0
    total_weight = sum(numbers)
    for score, weight in zip(scores, numbers):
        weighted_sum += score * weight
    weighted_average = "{:.6f}".format(weighted_sum / total_weight)
    return weighted_average


# 循环进入不同crf 编码质量的目录
for i in range(0, 52, 1):
    dis_path = "{}{}/".format("/dataset/dataset/reference_videos/crf/", i)
    output_path="/dataset/dataset/reference_videos/gops_middle_6/{}/".format(i)
    records = []
    for file in files:
        dir=file.split(".")[0]
        os.makedirs(os.path.join(output_path,dir, "target"), exist_ok=True)
        os.makedirs(os.path.join(output_path,dir, "source"), exist_ok=True)
        os.makedirs(os.path.join(output_path, dir, "vmaf"), exist_ok=True)

        source_dir = os.path.join(output_path, dir, "source")
        target_dir = os.path.join(output_path, dir, "target")
        vmaf_dir = os.path.join(output_path, dir, "vmaf")
    
        file_txt = file.split(".")[0] + ".txt"
        rate = float(subprocess.run(["mediainfo", "--Inform=Video;%FrameRate%", ref_path + file]
, stdout=subprocess.PIPE, universal_newlines=True).stdout.strip())
        play_time = round(1 / rate * 3, 3)
        
        start_time = time.time()

        data = []
        with open (os.path.join(gop_path, file_txt), "r") as f:
            lines = f.readlines()
            data = list(map(float, lines[0].split()))
        f.close()

        commands = []
        for idx, begin in enumerate(data):
                command = f"ffmpeg -ss {begin} -i {ref_path+file} -t {play_time} -map 0:0 -c:0 copy -map_metadata 0 -default_mode infer_no_subs -ignore_unknown -f mp4 -y {source_dir}/{idx}.mp4"
                commands.append(command)
                # print("当前执行指令1：{}".format(command))
                # subprocess.run(command, shell=True)
                command = f"ffmpeg -ss {begin} -i {dis_path+file} -t {play_time} -map 0:0 -c:0 copy -map_metadata 0 -default_mode infer_no_subs -ignore_unknown -f mp4 -y {target_dir}/{idx}.mp4"
                commands.append(command)
                # print("当前执行指令2：{}".format(command))
                # subprocess.run(command, shell=True)
        processes = []
        for command in commands:
            process = subprocess.Popen(command, shell=True)
            processes.append(process)
        
        for process in processes:
            process.wait()

        # f.close()
        print("finish {}".format(file))
        end_time = time.time()
        cut_time = "{:.2f}".format(end_time - start_time)
        print(f"finish cut {file} time: {cut_time}")

        # with open (os.path.join(gop_path, file_txt), "r") as f:
        #     lines = f.readlines()
        #     data = list(map(float, lines[0].split()))
        #     for idx, begin in enumerate(data):
        #         command = f"ffmpeg -ss {begin} -i {ref_path+file} -t {play_time} -map 0:0 -c:0 copy -map_metadata 0 -default_mode infer_no_subs -ignore_unknown -f mp4 -y {source_dir}/{idx}.mp4"
        #         print("当前执行指令1：{}".format(command))
        #         subprocess.run(command, shell=True)
        #         command = f"ffmpeg -ss {begin} -i {dis_path+file} -t {play_time} -map 0:0 -c:0 copy -map_metadata 0 -default_mode infer_no_subs -ignore_unknown -f mp4 -y {target_dir}/{idx}.mp4"
        #         print("当前执行指令2：{}".format(command))
        #         subprocess.run(command, shell=True)
        # f.close()
        # print("finish {}".format(file))
        # end_time = time.time()
        # # 记录裁剪视频的时间开销
        # cut_time = "{:.2f}".format(end_time - start_time)

# 第二步：对对应的GOP做vmaf计算，得到结果

        with concurrent.futures.ProcessPoolExecutor() as executor:
            slips = sorted(os.listdir(source_dir))
            futures = {executor.submit(run_vmaf, slip): slip for slip in slips}
            start_time = time.time()
            # 等待任务完成
            for future in futures:
                future.result()
            end_time = time.time()
        executor.shutdown()

        evaluate_time = "{:.2f}".format(end_time - start_time)
        print('finish all vmaf evaluate')

# 第三步：得到加权后的结果（计时结束）
        vmaf_slip_list = []
        count_list = []
        start_time = time.time()
        for vmaf_txt in sorted(os.listdir(vmaf_dir)):
            vmaf_txt_path = os.path.join(vmaf_dir, vmaf_txt)
            # 可以用shell写，也可以用python写，分别对比一下花费的时间
            # 这里先使用shell实现
            with open(vmaf_txt_path, "r") as f:
                lines = f.readlines()
                # 从vmaf的txt文件中提取vmaf分数
                vmaf_str = lines[5].split()[14]
                m = re.search(r'\d+(\.\d+)?', vmaf_str)
                vmaf = float(m.group(0))
                vmaf_slip_list.append(vmaf)
            f.close()
        # 获取每个slip的vmaf分数后，只需要获得对应的slip的帧数即可
        count_list = get_frame_number(file)
        print(count_list)
        result = calculate_final_vmaf(vmaf_slip_list, count_list)
        # print(result)
        
        end_time = time.time()
        if result == "100.000000":
            result = "100.00000"
        merge_time = "{:.2f}".format(end_time - start_time)
        total_time = "{:.2f}".format(float(cut_time) + float(evaluate_time) + float(merge_time))
        record = Record(file, result, total_time, cut_time, evaluate_time, merge_time)
        records.append(record)
        # print(f"filename: {file} vmaf: {result} total time: {total_time}, cut_time: {cut_time}, evaluate_time: {evaluate_time}, merge_time: {merge_time}")
    with open(os.path.join(result_path, "crf-{}.txt".format(i)), "w") as f:
        for record in records:
            f.write(record.get_str())
    f.close()
    records = []
    time.sleep(30)


# 第四步：将加权后的结果写入文件，得到最终的vmaf结果与时间开销
        # with open(os.path.join(output_path, dir, "result.txt"), "r") as f:


