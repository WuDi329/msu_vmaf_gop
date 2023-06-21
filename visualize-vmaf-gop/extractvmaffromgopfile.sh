# 从脏数据中剥离测量不准的vmaf，并且将其结果另存到visualize-vmaf-gop目录下的logfile_score_firstgop目录下
video_path=/dataset/dataset/reference_videos/output_16000k/reference_gop/
path=/home/wudi/desktop/dataset_operation/vmaf/logfile_firstgop/
dest_path=/home/wudi/desktop/dataset_operation/visualize-vmaf-gop/logfile_score_firstgop/
gop_path=/home/wudi/desktop/dataset_operation/extractgops/I-numbers-first/

files=$(ls $path)

for f in $files
do
  video="${f%.txt}_gop.mp4"
  # 获取每个视频的帧率，和每个视频的最大的准确帧号
  rate=$(mediainfo --Inform="Video;%FrameRate%" "$video_path$video")
  end_time=$(awk 'NR==1{print $2}' ${gop_path}${f})

  id=$(echo "scale=3; $end_time * $rate" | bc)
  id=$(printf "%.0f" $id)
  id=$(($id + 4))
  echo $id

  # cmd="NR>=5 && NR<=${id} {print \$2, \$15}"
  # echo "$f $rate $end_time $id"
  awk "NR>=5 && NR<=${id} {print \$2, \$15}" "$path$f" > "${dest_path}$f"
  # awk 'NF > 0' "${dest_path}tmp" > "${dest_path}${fname}"

  echo "finish $f file"
done