#!/bin/bash
# 作用是将visualize-vmaf-gop目录下的regenerate_gop_score.txt文件中的第一列替换到vmaf下的vmaf_result_16000k_firstgop.txt文件中的第一列
# 重新生成具有vmaf分数。处理时间和文件名的汇总文件
awk 'FNR==NR{a[NR]=$1;next}{$1=a[FNR]}1' regenerate_gop_score.txt ../vmaf/vmaf_result_16000k_firstgop.txt > temp.txt
awk '{gsub(/ /,"   ")}1' temp.txt > test.txt
rm temp.txt