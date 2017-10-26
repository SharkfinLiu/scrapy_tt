import re
import json

r = re.compile(r' \(\d+\)')  # 热敏电阻(2,585)
r_zh = re.compile(r'[\u4e00-\u9fa5]')
r_1 = re.compile(r'</a>')
r_gupiao = re.compile(r"{'(\d{6})':'(\S+)'}")
with open('ccccc', mode='r', encoding='utf-8') as f:
    f1 = f.readlines()
print(f1)
for line in f1:
    line = json.loads(line)
# target = {}
# for k, v in a.items():
#     target.update(dict([(s, k) for s in v]))
# print(target)

# for k,v in b.items():
# for line in f1:
#     line = line.replace("'", '"')
#     if line == '':
#         continue

#     if r_gupiao.search(line):
#         num = r_gupiao.search(line).group(1)
#         name = r_gupiao.search(line).group(2)
    #     line = re.sub(r_gupiao, '', line)
        # line = r_gupiao.search(line).group(1)
    # if line:
    #     line = line.split('	')
    #     line = line[0]
        # line = ''.join(line)
    with open('ccccc_1', mode='a+', encoding='utf-8') as f:
        f.write('%s\n'%line['name'])
        # f.write("'%s\t%s'," %(line. + '\n')
        # f.write("'%s'" % line + ":'Power Circuits'," +'\n')
        # f.write("'%s'" % k + ':' + "'%s'" % v + ','+ '\n')
        # f.write("'%s\t%s'," % (name,num) + '\n')
