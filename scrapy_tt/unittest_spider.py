# -*- coding:utf-8 -*-
import unittest
import re
from scrapy.crawler import CrawlerProcess
from scrapy_tt.spiders.yule_star import *
from scrapy_tt.spiders.dc3 import *
from scrapy_tt.spiders.dc3_for import *
from scrapy_tt.spiders.dc3_digui import *
from scrapy_tt.spiders.dc3_for_2 import *

class SpidersTestCase(unittest.TestCase):

    def test_YuleBiakeSpider_1(self):
        p = CrawlerProcess({})
        p.crawl(YuleBiakeSpider_1)
        p.start()
    def test_YuleBiakeSpider_2(self):
        p = CrawlerProcess({})
        p.crawl(YuleBiakeSpider_2)
        p.start()
    def test_YuleBiakeSpider_3(self):
        p = CrawlerProcess({})
        p.crawl(YuleBiakeSpider_3)
        p.start()
    def test_YuleBiakeSpider_4(self):
        p = CrawlerProcess({})
        p.crawl(YuleBiakeSpider_4)
        p.start()
    def test_YuleBiakeSpider_5(self):
        p = CrawlerProcess({})
        p.crawl(YuleBiakeSpider_5)
        p.start()
    def test_YuleBiakeSpider_6(self):
        p = CrawlerProcess({})
        p.crawl(YuleBiakeSpider_6)
        p.start()
    def test_YuleBiakeSpider_10(self):
        p = CrawlerProcess({})
        p.crawl(YuleBiakeSpider_10)
        p.start()
    def test_YuleBiakeSpider_7(self):
        p = CrawlerProcess({})
        p.crawl(YuleBiakeSpider_7)
        p.start()
    def test_YuleBiakeSpider_8(self):
        p = CrawlerProcess({})
        p.crawl(YuleBiakeSpider_8)
        p.start()
    def test_YuleBiakeSpider_9(self):
        p = CrawlerProcess({})
        p.crawl(YuleBiakeSpider_9)
        p.start()


    def test_YuleBiakeSpider_11(self):
        p = CrawlerProcess({})
        p.crawl(YuleBiakeSpider_11)
        p.start()

    def test_YuleBiakeSpider_12(self):
        p = CrawlerProcess({})
        p.crawl(YuleBiakeSpider_12)
        p.start()

    def test_dc3(self):
            # scr_list = '然后从前向后，每三个字符一组，即aba,aaa,ba0,baa,aab,a00，我们发现，他们分别是Suffix[1],Suffix[4],Suffix[7],Suffix[2],Suffix[5],Suffix[8] 的前3个字母。我们求出这六个的排名为4,2,5,6,3,1（注意，如果排序后还有相同的数字，也就是还有两个相同的串，比如3,2,4,5,2,1，那么要继续求，因为两个2之后的数字4大于1，所以第二的位置的2代表的后缀大于第5个位置的2代表的后缀。其实这个问题跟刚才的问题是相同的，所以可以递归求）。这样，我们最后得到了所有模3不等于0的位置的后缀的排名。|'
            # src_list = list(scr_list)
        # src_list = ['侠客岛', '特朗普', '访华', '前', '美国', '给', '中国', '送', '了', '份', '不大不小', '的', '礼物', '|', '特朗普', '访华', '前', '美国', '给', '中国', '送', '了', '份', '不大不小', '的', '礼物', '|', '特朗普', '访华', '前', '美国', '送', '了', '中国', '一份', '不大不小', '的', '礼物', '|']
        src_list = ['a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a']
        # src_list = ['1']
        s = []
        result_list = dc3_input(src_list)
        print(result_list)
        for i in result_list:
            for j in range(i, len(src_list)):
                s.append(src_list[j])
            print('sa[' + str(i) + ']')
            print(s)
            s = []


    def test_dc3_for(self):
            # scr_list = '然后从前向后，每三个字符一组，即aba,aaa,ba0,baa,aab,a00，我们发现，他们分别是Suffix[1],Suffix[4],Suffix[7],Suffix[2],Suffix[5],Suffix[8] 的前3个字母。我们求出这六个的排名为4,2,5,6,3,1（注意，如果排序后还有相同的数字，也就是还有两个相同的串，比如3,2,4,5,2,1，那么要继续求，因为两个2之后的数字4大于1，所以第二的位置的2代表的后缀大于第5个位置的2代表的后缀。其实这个问题跟刚才的问题是相同的，所以可以递归求）。这样，我们最后得到了所有模3不等于0的位置的后缀的排名。|'
            # src_list = list(scr_list)
        src_list = ['侠客岛', '特朗普', '访华', '前', '美国', '给', '中国', '送', '了', '份', '不大不小', '的', '礼物', '|', '特朗普', '访华', '前', '美国', '给', '中国', '送', '了', '份', '不大不小', '的', '礼物', '|', '特朗普', '访华', '前', '美国', '送', '了', '中国', '一份', '不大不小', '的', '礼物', '|']
        # src_list = ['a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a']
        # src_list = ['1']
        s = []
        result_list = dc3_for_input(src_list)
        print(result_list)
        for i in result_list:
            for j in range(i, len(src_list)):
                s.append(src_list[j])
            print('sa[' + str(i) + ']')
            print(s)
            s = []

    def test_sort_chinese(self):
        # src_list = ['|','利','反','媒','激','特','税','英','计','遭']
        src_list = ['侠客岛', '特朗普', '访华', '前', '美国', '给', '中国', '送', '了', '份', '不大不小', '的', '礼物', '|', '特朗普', '访华', '前',
                    '美国', '给', '中国', '送', '了', '份', '不大不小', '的', '礼物', '|', '特朗普', '访华', '前', '美国', '送', '了', '中国',
                    '一份', '不大不小', '的', '礼物', '|']
        src_list = list(set(src_list))
        src_list.sort()
        for i,val in enumerate(src_list):
            print(str(i)+':'+val)

    def test_q(self):
        count = 2
        left = "("
        right = ',)'
        blank = ''
        for _ in range(count):
            blank = left + blank
        blank = blank + "''"
        for _ in range(count):
            blank = blank + right
        print(blank)

    def test_dc3_digui(self):
        # scr_list = '然后从前向后，每三个字符一组，即aba,aaa,ba0,baa,aab,a00，我们发现，他们分别是Suffix[1],Suffix[4],Suffix[7],Suffix[2],Suffix[5],Suffix[8] 的前3个字母。我们求出这六个的排名为4,2,5,6,3,1（注意，如果排序后还有相同的数字，也就是还有两个相同的串，比如3,2,4,5,2,1，那么要继续求，因为两个2之后的数字4大于1，所以第二的位置的2代表的后缀大于第5个位置的2代表的后缀。其实这个问题跟刚才的问题是相同的，所以可以递归求）。这样，我们最后得到了所有模3不等于0的位置的后缀的排名。|'
        # src_list = list(scr_list)
        src_list = ['侠客岛', '特朗普', '访华', '前', '美国', '给', '中国', '送', '了', '份', '不大不小', '的', '礼物', '|', '特朗普', '访华', '前', '美国', '给', '中国', '送', '了', '份', '不大不小', '的', '礼物', '|', '特朗普', '访华', '前', '美国', '送', '了', '中国', '一份', '不大不小', '的', '礼物', '|']
        # src_list = ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a',
        #             'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a',
        #             'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a',
        #             'a']
        # src_list = ['1']
        s = []
        result_list = dc3_digui_input(src_list)
        print(result_list)
        for i in result_list:
            for j in range(i, len(src_list)):
                s.append(src_list[j])
            print('sa[' + str(i) + ']')
            print(s)
            s = []

    def test_dc3_for_2(self):

        # scr_list = '然后从前向后，每三个字符一组，即aba,aaa,ba0,baa,aab,a00，我们发现，他们分别是Suffix[1],Suffix[4],Suffix[7],Suffix[2],Suffix[5],Suffix[8] 的前3个字母。我们求出这六个的排名为4,2,5,6,3,1（注意，如果排序后还有相同的数字，也就是还有两个相同的串，比如3,2,4,5,2,1，那么要继续求，因为两个2之后的数字4大于1，所以第二的位置的2代表的后缀大于第5个位置的2代表的后缀。其实这个问题跟刚才的问题是相同的，所以可以递归求）。这样，我们最后得到了所有模3不等于0的位置的后缀的排名。|'
        # src_list = list(scr_list)
        src_list = ['侠客岛', '特朗普', '访华', '前', '美国', '给', '中国', '送', '了', '份', '不大不小', '的', '礼物', '|', '特朗普', '访华', '前',
                    '美国', '给', '中国', '送', '了', '份', '不大不小', '的', '礼物', '|', '特朗普', '访华', '前', '美国', '送', '了', '中国',
                    '一份', '不大不小', '的', '礼物', '|']
        # src_list = ['11','17','16','15','19','07','04','12','02','11','09','16','05','19','08','04','14','02','17','10','18','06','03','04','13','01']
        # src_list = ['a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a']
        # src_list = ['1']
        s = []
        result_list = dc3_input_for_2(src_list)
        print(result_list)
        for i in result_list:
            for j in range(i, len(src_list)):
                s.append(src_list[j])
            print('sa[' + str(i) + ']')
            print(s)
            s = []

    def test_selector(self):
        selector_css = 'body > table:nth-child(3) > tr:nth-child(1) > td:nth-child(2) > table:nth-child(4) >table:nth-child(0) > tr:nth-child(2) > .px12c > table > tr > td > div > founder-content *::text'
        css_re = re.compile(r'table[\-:()0-9a-zA-Z]*\s>')
        # add_tbody = ' tbody >'
        t = css_re.finditer(selector_css)
        # count = 0
        # for i in t:
        #     count += 1
        # print(count)
        star =[]
        end =[]
        for i in t:
            star.append(i.span()[0])
            end.append(i.span()[-1])
            # add_tbody = i.group() + ' tbody >'
        print(star)
        print(end)
        list_len = len(star)
        table = []
        other = []
        other.append(selector_css[:star[0]])
        for i in range(list_len):
            if i <list_len-1:
                other.append(selector_css[end[i]:star[i+1]])
            table.append(selector_css[star[i]:end[i]])
        other.append(selector_css[end[-1]:])
        # print(count)
        # star.append(selector_css[:i.span()[0]])
        # end.append(selector_css[i.span()[-1]:])
        print(other)
        print(table)

    def test_plzh(self):
        import itertools
        add_tbody = ' tbody >'
        list1 = [1, 2, 3]
        list2 = []
        for i in range(1, len(list1) + 1):
            iter = itertools.combinations(list1, i)
            list2.append(list(iter))
        for lis in list2:
            for li in lis:
                print(list(li))