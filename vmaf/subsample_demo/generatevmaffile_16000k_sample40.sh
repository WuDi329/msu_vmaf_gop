#!/bin/bash
# NOTE : Quote it else use array to avoid problems #
path=/dataset/dataset/reference_videos/
files=$(ls $path | grep '\.mp4$')
# output_path=/data/wd/dataset/dataset/reference_videos/new_output/
output_path=/dataset/dataset/reference_videos/output_16000k/
score_path=/dataset/dataset/reference_videos/ffmpeg-score/
final=''
for f in $files
do
  
#   echo "Processing $f file..."
#   判断的时候记得进行字符串拼接
  if [ -d "$path$f" ]
  then
    # ffmpeg -i "$file" -c:v libx264 -preset slow -crf 22 -c:a copy "${file%.mp4}.mkv"
    # rm "$file" # optional: delete original file after conversion
    echo "$path$f is not a mp4"
  else
    # 获取时间基
    # time_base=`ffprobe "$path$f" -show_streams -select_streams v -print_format csv -loglevel fatal | cut -d ',' -f 30`
    # echo "current video time_base is $time_base"

    # 替换$f
    f264="${f%.mp4}_264.mp4"

    # 第一步：生成file
     /usr/bin/time ffmpeg -i "$output_path$f264" -i "$path$f" -lavfi "[0:v][1:v]libvmaf=psnr=1:n_subsample=40:log_path=/home/wudi/desktop/dataset_operation/vmaf/logfile_sample40/${f}.txt" -f null -

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
  fi
  echo "finish $f file"

  # take action on each file. $f store current file name
#   cat "$f"
done