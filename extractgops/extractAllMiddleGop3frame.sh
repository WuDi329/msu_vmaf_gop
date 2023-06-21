#!/bin/bash
# 此模块的功能是根据GOP的范围将源视频和重新编码视频的中间三帧生成视频段。
# 第一步：抽取不同的gop
ref_path=/dataset/dataset/reference_videos/
files=$(ls $ref_path | grep '\.mp4$')
# output_path=/data/wd/dataset/dataset/reference_videos/new_output/
output_path=/dataset/dataset/reference_videos/output_16000k/gops_middle/

gop_path=/home/wudi/desktop/dataset_operation/I-numbers-middle/

for i in $(seq 0 51); do
  dis_path="/dataset/dataset/reference_videos/crf/${i}/"
  output_path="/dataset/dataset/reference_videos/crf/${i}/gops_middle/"
  for f in $files
  do
    
  #   echo "Processing $f file..."
  #   判断的时候记得进行字符串拼接
    if [ -d "$ref_path$f" ]
    then
      # ffmpeg -i "$file" -c:v libx264 -preset slow -crf 22 -c:a copy "${file%.mp4}.mkv"
      # rm "$file" # optional: delete original file after conversion
      echo "$ref_path$f is not a mp4"
    else
      # 获取时间基
      # time_base=`ffprobe "$path$f" -show_streams -select_streams v -print_format csv -loglevel fatal | cut -d ',' -f 30`
      
      # echo "current video time_base is $time_base"

      dir=${f%.mp4}
      mkdir -p ${output_path}${dir}/target
      mkdir -p ${output_path}${dir}/source
      # 替换$f
      f264="${f%.mp4}_264.mp4"
      filename="${f%.mp4}.txt"

      fgop="${f%.mp4}_gop.mp4"
      f264gop="${f%.mp4}_264_gop.mp4"

      
      rate=$(mediainfo --Inform="Video;%FrameRate%" "$ref_path$f")
      # echo "lalalal"
      # echo $rate

      last_time=$(echo "scale=3; 1 / $rate * 3" | bc | awk '{printf "%.3f", $0}')
      echo $last_time

      time=$(awk 'NR==1{for(i=1;i<=NF;i++) if($i~/^[0-9]+(\.[0-9]+)?$/) print $i}' "${gop_path}${filename}")
      echo $time
      for col in $time
      do
        # col=$(echo "${col%$'\r'}") # 删除回车符
        echo $col;
        ffmpeg -hide_banner -ss ${col} -i ${ref_path}${f} -t ${last_time} -map 0:0 -c:0 copy -map_metadata 0 -default_mode infer_no_subs -ignore_unknown -f mp4 -y ${output_path}${dir}/source/${i:-0}.mp4;
        ffmpeg -hide_banner -ss ${col} -i ${dis_path}${f264} -t ${last_time} -map 0:0 -c:0 copy -map_metadata 0 -default_mode infer_no_subs -ignore_unknown -f mp4 -y ${output_path}${dir}/target/${i:-0}.mp4;
        i=$((i+1))
      done
      unset i

      

    fi
    echo "finish $f file"

    # take action on each file. $f store current file name
  #   cat "$f"
  done
done