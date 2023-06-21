# ref_output_path=/dataset/dataset/reference_videos/output_sameIF_16000k/reference_gop/
# dis_output_path=/dataset/dataset/reference_videos/output_sameIF_16000k/distorted_gop/
# 这个模块的作用是比较源视频和重新编码视频的GOP是否相同
ref_output_path=/dataset/dataset/reference_videos/output_16000k/reference_gop/
dis_output_path=/dataset/dataset/reference_videos/output_16000k/distorted_gop/

files=$(ls $ref_output_path | grep '\.mp4$')

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
    f264gop="${f%_gop.mp4}_264_gop.mp4"

    ffprobe -select_streams v -show_entries packet=pts_time -of csv=print_section=0 ${ref_output_path}${f} > temp.txt
    source=$(awk 'END{print}' temp.txt)

    ffprobe -select_streams v -show_entries packet=pts_time -of csv=print_section=0 ${dis_output_path}${f264gop} > temp.txt
    target=$(awk 'END{print}' temp.txt) 

    echo "$f $source, $target" >> res.txt
    

  fi
  echo "finish $f file"

  # take action on each file. $f store current file name
#   cat "$f"
done