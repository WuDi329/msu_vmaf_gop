from datetime import datetime, timedelta
from decimal import Decimal, ROUND_HALF_UP
import os
import re

output_path = "/home/wudi/desktop/vmaf_gop_test/crf_vmaf_avg/"
ref_path = "/home/wudi/desktop/vmaf_gop_test/crf_vmaf_2/"
ref_path2 = "/home/wudi/desktop/vmaf_gop_test/crf_vmaf/"
ref_path3 = "/home/wudi/desktop/vmaf_gop_test/crf_vmaf_3/"


def read_vmaf_time(vmaf_path): 
    all_scores = []
    with open(vmaf_path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            elements = line.split(' ')
            time_str = elements[3]
            time_obj = datetime.strptime(time_str, '%M:%S.%f')
            time_float = time_obj.minute * 60 + time_obj.second + time_obj.microsecond / 1000000
            all_scores.append(Decimal(str(time_float)))
    # print(all_scores)
    return all_scores



def read_vmaf_path(vmaf_path): 
    path = []

    with open(vmaf_path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            elements = line.split(' ')
            # print(elements)
            path.append(elements[6].strip('\n'))
    # print(all_scores)
    return path

def read_vmaf_score(vmaf_path):
    all_scores = []
    with open(vmaf_path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            m = re.search(r'^\d+(\.\d+)?', line)
            if m:
                vmaf = float(m.group(0))
                all_scores.append(vmaf)
    # print(all_scores)
    return all_scores


for path in sorted(os.listdir(ref_path)):


    scores = read_vmaf_score(ref_path+path)
    # print(scores)

    paths = read_vmaf_path(ref_path+path)


    # score1 = []
    # score2 = []
    # score3 = []
    time1 = read_vmaf_time(ref_path + path)
    print(time1)
    print('\n')
    time2 = read_vmaf_time(ref_path2 + path)
    print(time2)
    print('\n')
    time3 = read_vmaf_time(ref_path3 + path)
    print(time3)
    print('\n')
    # times = [time1, time2, time3]
    times = [time1, time2, time3]
    # print(scores)
    avg_time = [sum(x) / len(x) for x in zip(*times)]
    print('\n')
    # print(avg_time)
    rounded_avg_time = [x.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP) for x in avg_time]
    print(rounded_avg_time)
    # time_strs = []
    # # time_strs = [timedelta(seconds=float(x)).strftime('%M:%S.%f') for x in rounded_avg_score]

    # for x in rounded_avg_time:
    #     minutes, seconds = divmod(x, 60)
    #     seconds = int(seconds)
    #     microseconds = (x - int(x)) * 1000000
    #     time_str = '{:02d}:{:05.2f}'.format(int(minutes), seconds + microseconds / 1000000)
    #     time_strs.append(time_str)
    
    with open(os.path.join(output_path, path), 'w') as f:
        for i in range(len(scores)):
            f.write(str(scores[i]) + '    '+  str(rounded_avg_time[i]) + '    ' + paths[i] + '\n')
    f.close()

