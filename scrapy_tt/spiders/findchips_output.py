# -*- coding: utf-8 -*-
# import scrapy
#
#
# class AaaSpider(scrapy.Spider):
#     name = 'aaa'
#     allowed_domains = ['aaa.com']
#     start_urls = ['http://aaa.com/']
#
#     def parse(self, response):
#         pass
# from scrapy_tt.spiders.proxy_count import proxy_count
#
# print(proxy_count('asdf'))
import re
import json

# r_title = re.compile(r'"title": "(\w+)"')
lis = []
with open('finchips.json', mode='r', encoding='utf-8') as f:
    f1 = f.readlines()
for line in f1:
    l = json.loads(line)
    lis.append(l['title'])
    # print(lis)
    # if r_title.search(line):
    #     lis.append(r_title.search(line).group(1))

# print(f1)
# print(len(f))
print(len(lis))
lis_set = set(lis)
print(len(lis_set))
# print(lis_set)
lis_set_list = list(lis_set)
print(lis_set_list)

lis_set_list.sort()  # 排序

print(lis_set_list)
for line in lis_set_list:
    with open('finchips_set_1', mode='a+', encoding='utf-8') as f:
        f.write(line + '\n')

