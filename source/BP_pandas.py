import os
import pandas as pd

def findnth(source, target, n):
    num = 0
    start = -1
    while num < n:
        start = source.find(target, start+1)
        if start == -1: return -1
        num += 1
    return start

def replacenth(source, old, new, n):
    p = findnth(source, old, n)
    if n == -1: return source
    newline = source[:p] + new + source[p+len(old):]
    return newline

match = ','
erase_num = 4
cnt = 0
with open('C:\\dev\\workspace\\Blueprism\\BPVWorkQueueItem.csv', 'r') as rf:
    with open('C:\\dev\\workspace\\Blueprism\\BPVWorkQueueItem_out.csv', 'w') as wf:
        for line in rf:
            cnt += 1
            num_comma = len(line.split(match)) - 1
            while num_comma > 14:
                line=replacenth(line, ',', '', 4)
                num_comma = len(line.split(match)) - 1
            wf.write(line)

cvs_file = os.path.join('C:\\dev\\workspace\\Blueprism\\', 'BPVWorkQueueItem_out.csv')
df = pd.read_csv(cvs_file, encoding = "ISO-8859-1")
df_2 = pd.read_csv(cvs_file, usecols=[1])
df_2 = pd.read_csv(cvs_file, usecols=[2])
df_items = pd.read_csv(cvs_file, encoding = "ISO-8859-1", usecols=['keyvalue'])





