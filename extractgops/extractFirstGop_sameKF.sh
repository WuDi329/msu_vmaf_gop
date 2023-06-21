#!/bin/bash
# 此模块的功能是将源视频和重新编码视频（保持着相同的关键帧）的第一个GOP生成视频段。
# NOTE : Quote it else use array to avoid problems #
ref_path=/dataset/dataset/reference_videos/
dis_path=/dataset/dataset/reference_videos/output_sameIF_16000k/
files=$(ls $ref_path | grep '\.mp4$')
# output_path=/data/wd/dataset/dataset/reference_videos/new_output/
ref_output_path=/dataset/dataset/reference_videos/output_sameIF_16000k/reference_gop/
dis_output_path=/dataset/dataset/reference_videos/output_sameIF_16000k/distorted_gop/

gop_path=/home/wudi/desktop/dataset_operation/extractgops/I-numbers-first/

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
    filename="${f%.mp4}.txt"

    fgop="${f%.mp4}_gop.mp4"
    f264gop="${f%.mp4}_264_gop.mp4"

    start_time=$(awk 'NR==1{print $1}' ${gop_path}${filename})
    end_time=$(awk 'NR==1{print $2}' ${gop_path}${filename})

    # 抽取GOP的指令
    ffmpeg -ss ${start_time} -to ${end_time} -i ${ref_path}${f} -map 0:0 -c:0 copy -map_metadata 0 -default_mode infer_no_subs -ignore_unknown -f mp4 -y ${ref_output_path}${fgop}
    ffmpeg -ss ${start_time} -to ${end_time} -i ${dis_path}${f264} -map 0:0 -c:0 copy -map_metadata 0 -default_mode infer_no_subs -ignore_unknown -f mp4 -y ${dis_output_path}${f264gop}

    

  fi
  echo "finish $f file"

  # take action on each file. $f store current file name
#   cat "$f"
done