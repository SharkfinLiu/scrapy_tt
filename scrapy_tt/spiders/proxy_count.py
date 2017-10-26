import re
import time
import json


def proxy_count(filename):

    with open(filename, mode='r', encoding='utf-8') as f:
        f1 = f.readlines()
    count = 0
    count_set = 0
    lines_ip = []
    lines_ip_count =[]
    r_ip = re.compile(r'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}:[0-9]+')
    r_count = re.compile(r"'count': (\d+)")

    for line in f1:
        if r_ip.search(line):
            s = r_ip.search(line).group()
            lines_ip.append(s)  # 取出ip放在lines_ip
            if r_count.search(line):
                d = r_count.search(line).group(1)
                lines_ip_count.append(d) #取出count 放在另一个lines_ip_count    //这两个索引对应的数据是同一条
            else:
                lines_ip_count.append('0') #不存在为0

    lines_ip_set = set(lines_ip) #去重
    if len(lines_ip_set) == 0:
        return []
    lines_ip_set_count = [0 for i in range(len(lines_ip_set))]
    lines_ip_set_num = [0 for i in range(len(lines_ip_set))]
    ip_dict = [0 for i in range(len(lines_ip_set))]
    # 统计count和num
    for line_ip_set in lines_ip_set:
        for line_ip in lines_ip:
            if line_ip_set == line_ip:
                lines_ip_set_count[count_set] += int(lines_ip_count[count])
                lines_ip_set_num[count_set] += 1
            count += 1
        count_set += 1
        count = 0

    count = 0  # 初始化值

    for line in lines_ip_set:
        ip_dict[count] = {"ip": line, "count": lines_ip_set_count[count], "num": lines_ip_set_num[count]}
        count += 1
    # 排序
    ip_dict.sort(key=lambda k: (k.get('count', 0)), reverse=True)
    return ip_dict

    # 输出文件
    # for line in ip_dict:
    #     with open("Proxy_count", mode='a+', encoding='utf-8') as f:
    #         line = json.dumps(line, ensure_ascii=True) + "\n"
    #         f.write(line)



    # print(ip_dict)
    # print(len(lines_ip_set_num))
    # print(len(lines_ip_set_count))
