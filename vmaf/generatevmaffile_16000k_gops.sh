#!/bin/bash
# 第二部：进行vmaf分析
path=/dataset/dataset/reference_videos/output_16000k/gops_middle/



files=$(ls $path)
for f in $files
do
    # 现在进入每个视频文件夹
    fname=$path$f
    mkdir -p ${fname}/vmaf

    reference_gop=${fname}/source/
    distorted_gop=${fname}/target/
    vmaf_gop=${fname}/vmaf/

    videos=$(ls $reference_gop)
    for video in $videos
    do
        # 运行vmaf算法计算质量分数
        /usr/bin/time ffmpeg -i "$distorted_gop$video" -i "$reference_gop$video" -lavfi "[0:v][1:v]libvmaf=psnr=1:n_threads=3:log_path=${vmaf_gop}${video}.txt" -f null -
    done

    

    # 第二部：分别获取两个视频的所有关键帧


    # 第三步：使用关键帧生成图片，使用图片运行相应算法。


    # 第三步：将关键帧与对用的视频使用相应算法进行对比得到结果。

    # ffmpeg psnr score
    # /usr/bin/time ffmpeg -nostats -i "$output_path$f264" -i "$path$f" -lavfi psnr -loglevel info -f null - 2> psnr_output_16000k.txt
    # avg_psnr=$(awk '{a[NR]=$0}END{print a[NR-2]}' psnr_output_16000k.txt | awk '{print $8}' )
    # avg_psnr=${avg_psnr#average:}

    # exe_time=$(awk '{a[NR]=$0}END{print a[NR-1]}' psnr_output_16000k.txt | awk '{print $3}')
    # exe_time=${exe_time%elapsed}

    # echo "$avg_psnr   $exe_time   $f" >> psnr_result_16000k.txt

    # 计算ffmpeg vmaf score
    # echo ${time_base: 2}

    # 更改时间基使用硬件加速编码
    # ffmpeg -hwaccel_device 0 -hwaccel cuvid -c:v hevc_cuvid -i "$path$f" -vsync 0 -enc_time_base -1 -video_track_timescale ${time_base: 2} -c:v h264_nvenc "$output_path$f"
  
  echo "finish $f file"

  # take action on each file. $f store current file name
#   cat "$f"
done