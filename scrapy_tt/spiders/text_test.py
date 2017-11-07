import re
import json

r = re.compile(r' \(\d+\)')  # 热敏电阻(2,585)
r_zh = re.compile(r'[\u4e00-\u9fa5]')
r_1 = re.compile(r'</a>')
r_gupiao = re.compile(r"{'(\d{6})':'(\S+)'}")
r_zhengzhi = re.compile(r'([\u4e00-\u9fa5]+)：([\u4e00-\u9fa5,·]+)')
r_chengyu = re.compile(r'<[-,",A-Z,a-z,0-9,=,;,:,\s,/,%,宋体,\.]+>')
r_chengyu_2 = re.compile(r'【[\u4e00-\u9fa5]+】')
r_yule_1 = re.compile(r'^[\u4e00-\u9fa5]{2,}$') ## 牛好aaaaaaa咪\n
r_yule_2 = re.compile(r'^[A-Z,a-z]{3,}$')
r_yule_3 = re.compile(r'[\.,0-9,(,),\',\,,~,`,_]')
r_yule_4 = re.compile(r'\*')

with open('ccccc', mode='r', encoding='utf-8') as f:
    f1 = f.readlines()
print(f1)

# print("1\n")
# print(len(f1))
f1 = list(set(f1))
# f1.sort(key=lambda x: len(x))
# f1 = sorted(f1)
# print("2\n")
# print(len(set(f1)))

# print(f1)
# for line in f1:
#     line = json.loads(line)
# target = {}
# for k, v in a.items():
#     target.update(dict([(s, k) for s in v]))
# print(target)

# for k,v in b.items():
for line in f1:
    if line:
        line = line.replace('\n','')
        line = re.sub('\s*','',line)

        if line == '':
            continue

        # line = line.split(' ')[0]

    # line1 = line.split('——')
    # line1 = line1[-1]
    # line = line.split("：")
    # line1 = line[-1].split('·')
    # line1 = line1[-1]

    # line1 = line[-1].split("\t")
    # line = re.sub('（', '(', line)
    # line = re.sub('）',')',line)
    # line0 = line1[0]
    # line1 = line1[-1]
    # line2 = line[2]
    # line0 = re.sub('\s*','',line0)
    # line1 = re.sub('\s*','',line1)
    # line2 = re.sub('\s*','',line2)

    # if r_zhengzhi.search(line):
    #     line = r_zhengzhi.search(line).group()
    # else:
    #     continue
#         name = r_gupiao.search(line).group(2)
#         line = re.sub(r_chengyu_2, '', line)
        # line = r_gupiao.search(line).group(1)
    # if line:
    #     line = line.split('\t')
    #     line = line[0]
    #     # line = ''.join(line)
    #     for line2 in line1:
    # if r_yule_2.match(line):
    # if r_yule_4.search(line):
        with open('ccccc_3', mode='a+', encoding='utf-8') as f:
            # f.write('%s 99 nr\n%s 99 nr\n'%(line0,line1))
            f.write('%s 99 nr\n' % line)
        # f.write("'%s\t%s'," %(line. + '\n')
        #     f.write("'%s'" % line + ":'Diodes'," +'\n')
        # f.write("'%s'" % k + ':' + "'%s'" % v + ','+ '\n')
        # f.write("'%s\t%s'," % (name,num) + '\n')
    # if line1 == '':
    #     continue
    # with open('ccccc_2', mode='a+', encoding='utf-8') as f1:
    #     # f.write('%s 99 ntc\n%s 99 nt\n%s 99 nz\n'%(line0,line1,line2))
    #     f1.write('%s 99 nt\n'%line1)
    # else:
    #     with open('ccccc_2', mode='a+', encoding='utf-8') as f:
    #         # f.write('%s 99 nr\n%s 99 nr\n'%(line0,line1))
    #         f.write('%s\n' % line)