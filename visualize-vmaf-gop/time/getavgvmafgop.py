from datetime import datetime, timedelta
from decimal import Decimal, ROUND_HALF_UP
import os
import re

output_path = "/home/wudi/desktop/vmaf_gop_test/crf_vmaf_gop_avg/"
ref_path = "/home/wudi/desktop/vmaf_gop_test/crf_vmaf_gop4/"
ref_path2 = "/home/wudi/desktop/vmaf_gop_test/crf_vmaf_gop5/"
ref_path3 = "/home/wudi/desktop/vmaf_gop_test/crf_vmaf_gop6/"


def read_vmaf_time(vmaf_path):
    all_time = []
    cut_time = []
    eval_time = []
    merge_time = []
    with open(vmaf_path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            elemets = line.split(' ')
            print(elemets)
            all_time.append(float(elemets[7]))
            cut_time.append(float(elemets[13]))
            eval_time.append(float(elemets[17]))
            merge_time.append(float(elemets[21]))
    # print(all_scores)
    return all_time, cut_time, eval_time, merge_time



def read_vmaf_path(vmaf_path): 
    path = []

    with open(vmaf_path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            elements = line.split(' ')
            # print(elements)
            path.append(elements[-1].strip('\n'))
    # print(all_scores)
    return path

def read_vmaf_gops(vmaf_path):
    all_scores = []
    with open(vmaf_path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            elemets = line.split(' ')
            all_scores.append(elemets[1])
    # print(all_scores)
    return all_scores



# paths = read_vmaf_path(ref_path+'crf-0.txt')
# print(paths)

# time, cut_time, eval_time, merge_time = read_vmaf_time(ref_path + 'crf-0.txt')
# print(time)
# print(cut_time)
# print(eval_time)
# print(merge_time)


for path in sorted(os.listdir(ref_path)):
    # time = []
    # cut_time = []
    # eval_time   = []
    # merge_time = []
    time, cut_time, eval_time, merge_time = read_vmaf_time(ref_path + path)
    time1, cut_time1, eval_time1, merge_time1 = read_vmaf_time(ref_path2 + path)
    time2, cut_time2, eval_time2, merge_time2 = read_vmaf_time(ref_path3 + path)
    times = [time, time1, time2]
    cut_times = [cut_time, cut_time1, cut_time2]
    eval_times = [eval_time, eval_time1, eval_time2]
    merge_times = [merge_time, merge_time1, merge_time2]

    scores = read_vmaf_gops(ref_path+path)
    # print(scores)

    paths = read_vmaf_path(ref_path+path)

    # print(scores)
    avg_time = [round(sum(x) / len(x), 2) for x in zip(*times)]
    avg_cut_time = [round(sum(x) / len(x), 2) for x in zip(*cut_times)]
    avg_eval_time = [round(sum(x) / len(x), 2) for x in zip(*eval_times)]
    avg_merge_time = [round(sum(x) / len(x), 2) for x in zip(*merge_times)]

    # print('\n')
    # print(avg_time)
    # rounded_avg_time = [x.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP) for x in avg_time]
    # time_strs = []
    # time_strs = [timedelta(seconds=float(x)).strftime('%M:%S.%f') for x in rounded_avg_score]

    # for x in rounded_avg_time:
    #     minutes, seconds = divmod(x, 60)
    #     seconds = int(seconds)
    #     microseconds = (x - int(x)) * 1000000
    #     time_str = '{:02d}:{:05.2f}'.format(int(minutes), seconds + microseconds / 1000000)
    #     time_strs.append(time_str)
    
    with open(os.path.join(output_path, path), 'w') as f:
        for i in range(len(avg_time)):
            f.write("vmaf: {}    total time: {}    cut time: {}   evaluate_time: {}   merge_time: {}   {}\n".format(scores[i], avg_time[i], avg_cut_time[i], avg_eval_time[i], avg_merge_time[i], paths[i]))
    f.close()

