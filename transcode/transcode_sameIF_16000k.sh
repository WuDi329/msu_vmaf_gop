#!/bin/bash
# NOTE : Quote it else use array to avoid problems #
path=/dataset/dataset/reference_videos/
files=$(ls $path | grep '\.mp4$')
output_path=/dataset/dataset/reference_videos/output_sameIF_16000k/
time_path=/home/wudi/desktop/dataset_operation/I-numbers-py/

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

    # 计算倒数
    # echo ${time_base: 2}
    f264="${f%.mp4}_264.mp4"
    filename="${f%.mp4}.txt"

    # 获取具体的时间
    time=$(awk 'NR==1' "${time_path}${filename}")


    # 更改时间基使用硬件加速编码

    # 根据上面的关键帧数进行转码
    ffmpeg  -i "$path$f"  -c:v libx264 -b:v 16000k -force_key_frames "$time" -x264-params scenecut=-1 "$output_path$f264"

    unset str
  fi
  echo "finish $f file"

  # take action on each file. $f store current file name
#   cat "$f"
done