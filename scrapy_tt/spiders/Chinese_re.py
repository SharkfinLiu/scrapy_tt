import re
import time
import sys

file_open_path = sys.argv[1]  # '/home/pzzh/下载/entities'
with open(file_open_path, mode='r', encoding='utf-8') as f:
    f1 = f.readlines()

## 有中文就输出
# p = re.compile(r'[\u4e00-\u9fa5]')
# for line in f1:
#     if p.search(line):
#         with open(file_save_path, mode='a+', encoding='utf-8') as f:
#             f.write(line)


## 只有中文才输出
file_save_path = sys.argv[2]  # '/home/pzzh/下载/entities_chinese'
count = 0
p = re.compile(r'^[\u4e00-\u9fa5]+$')
start = time.time()
for line in f1:
    for i in re.split('\s', line):
        if p.search(i):
            with open(file_save_path, mode='a+', encoding='utf-8') as f:
                f.write(line)
            count += 1
end = time.time()
print('time=', end - start)
print('count=', count)
