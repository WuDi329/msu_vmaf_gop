import subprocess
import time
import os
# 补充实验，计算开销
path="/dataset/dataset/reference_videos/output_16000k/gops_middle/"


for f_name in sorted(os.listdir(path)):

    # 现在进入每个视频文件夹

    reference_gop = os.path.join(path, f_name, 'source')


    distorted_gop=os.path.join(path, f_name, 'target')
    

    start_time = time.time()
    for slip in sorted(os.listdir(reference_gop)):
        video = os.path.join(distorted_gop, slip)
        vmaf_gop = os.path.join(path, f_name, 'vmaf')
        command = 'ffmpeg -i "{}" -i "{}" -lavfi "[0:v][1:v]libvmaf=psnr=1:log_path={}.txt" -f null -'.format(video, os.path.join(reference_gop, slip), os.path.join(vmaf_gop, slip))
        subprocess.run(command, shell=True)
    print(f'finish {f_name}')
    print(f'finish {f_name}')
    print(f'finish {f_name}')
    print(f'finish {f_name}')
    print(f'finish {f_name}')
    print(f'finish {f_name}')
    end_time = time.time()
    elapsed_time = end_time - start_time
    elapsed_time_str = elapsed_time_str = '{:02d}:{:06.3f}'.format(int(elapsed_time // 60), elapsed_time % 60)
    with open('/home/wudi/desktop/dataset_operation/visualize-vmaf-gop/time-origin.txt', 'a') as f:
        f.write(elapsed_time_str + '\n')
    f.close()

