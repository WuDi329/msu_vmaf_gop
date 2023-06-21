#!/bin/bash
# NOTE : Quote it else use array to avoid problems #
path=/dataset/dataset/reference_videos/
files=$(ls $path | grep '\.mp4$')

for i in $(seq 0 51); do
    mkdir /dataset/dataset/reference_videos/crf/${i}/
    output_path="/dataset/dataset/reference_videos/crf/${i}/"
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

        ffmpeg  -i "$path$f"  -c:v h264 -crf ${i} "$output_path$f"
    fi
    echo "finish $i quality $f file"

    # take action on each file. $f store current file name
    #   cat "$f"
    done
    echo "finish $i quality"
done