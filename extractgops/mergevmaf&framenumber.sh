#!/bin/bash
# 这个模块的作用是将每个视频段对应的vmaf分数和它对应的帧数整合起来，写入到vmaf&numbers_middle中
# 第四步，将vmaf分数和每个片段的帧数整合到一起，主要修改下面两行
vmaf_path=/dataset/dataset/reference_videos/output_16000k/gops_middle/
output_path=/home/wudi/desktop/dataset_operation/vmaf\&numbers_middle/
number_path=/home/wudi/desktop/dataset_operation/Numberofframes/

files=$(ls $vmaf_path)
for f in $files
do
    # 现在进入每个视频文件夹
    fname=$vmaf_path$f

    vmaf_gop=${fname}/result.txt

    filename=${f}.txt

    scores=$(ls $vmaf_gop)
    for score in $scores
    do
        # 提取vmaf分数到${fname}/result.txt
        awk '{print $1}' ${vmaf_gop} > /home/wudi/desktop/dataset_operation/extractgops/temp1.txt
        awk '{print $1}' ${number_path}${filename} > /home/wudi/desktop/dataset_operation/extractgops/temp2.txt
        paste /home/wudi/desktop/dataset_operation/extractgops/temp1.txt /home/wudi/desktop/dataset_operation/extractgops/temp2.txt >> ${output_path}${filename}
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

rm /home/wudi/desktop/dataset_operation/extractgops/temp1.txt
rm /home/wudi/desktop/dataset_operation/extractgops/temp2.txt