# -*- coding:utf-8 -*-
import unittest
from scrapy.crawler import CrawlerProcess
from scrapy_tt.spiders.yule_star import *
from scrapy_tt.spiders.dc3 import *
from scrapy_tt.spiders.dc3_for import *
from scrapy_tt.spiders.dc3_digui import *

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
        # src_list = ['侠客岛', '特朗普', '访华', '前', '美国', '给', '中国', '送', '了', '份', '不大不小', '的', '礼物', '|', '特朗普', '访华', '前', '美国', '给', '中国', '送', '了', '份', '不大不小', '的', '礼物', '|', '特朗普', '访华', '前', '美国', '送', '了', '中国', '一份', '不大不小', '的', '礼物', '|']
        src_list = ['a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a']
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
        src_list = ['使用','cookie','登陆','比较','简单','，','但是','有','时效性','问题','。','验证码','识别','是','个','很好','的','思路','，','然而','识别','的','精度','又','限制','了','抓取','的','效率','。','使用','cookie','登陆','比较','简单','，']
        src_list = list(set(src_list))
        src_list.sort()
        print(src_list)

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