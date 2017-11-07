# -*- coding:utf-8 -*-
import unittest
from scrapy.crawler import CrawlerProcess
from scrapy_tt.spiders.yule_star import *

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