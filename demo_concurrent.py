import concurrent.futures
import subprocess
import os
import time

source_dir = "/dataset/dataset/reference_videos/"
target_dir = "/dataset/dataset/reference_videos/output_16000k/"

def run_vmaf(file):
    command = 'ffmpeg -i "{}" -i "{}" -lavfi "[0:v][1:v]libvmaf=psnr=1" -f null -'.format(os.path.join(source_dir, file), os.path.join(target_dir, file.split(".")[0] + "_264.mp4"))
    subprocess.run(command, shell=True)

start = time.time()
with concurrent.futures.ProcessPoolExecutor() as executor:
    slips = sorted(os.listdir(source_dir))
    futures = {executor.submit(run_vmaf, slip): slip for slip in slips}

    # 等待任务完成
    for future in futures:
        future.result()

print('finish all')
end = time.time()
print('time cost: ', end - start)
    # for slip in sorted(os.listdir(source_dir)):
    #     run_vmaf(slip)
    #     executor.submit(subprocess.run, ["python3", "run_vmaf.py", "-r", "/dataset/dataset/reference_videos/gops_middle/{}/".format(i), "-t", "/dataset/dataset/target_videos/", "-s", "/dataset/dataset/vmaf_result_middle/{}/".format(i), "-g", gop_path, "-f", file_txt])
    #     print("finish {}".format(file))

