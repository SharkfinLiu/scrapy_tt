# -*- coding:utf-8 -*-
from scrapy.crawler import CrawlerProcess
# from quanjingwang.spiders.p5w import P5wSearchSpider
# from quanjingwang.spiders.guancha import GuanchaSearchSpider
# from quanjingwang.spiders.ob import ObSpider
# from quanjingwang.spiders.chinaso import  ChinasoSearchSpider
# from quanjingwang.spiders.chinanews import ChinanewsSearchSpider
# from quanjingwang.spiders.xfrb import XfrbSearchSpider
# from quanjingwang.spiders.huanqiu import HuanqiuSearchSpider
# from quanjingwang.spiders.gmw import GmwSeacherSpider
from scrapy_tt.spiders.spider_baike import SpiderBaikeSpider
from scrapy_tt.spiders.findchips import FindchipsSpider
from scrapy_tt.spiders.testspider import TestSpider
from scrapy_tt.spiders.test_phantomjs import Test_Phantomjs_SearchSpider
from scrapy_tt.spiders.gupiao import *
from scrapy_tt.spiders.itjuzi import *

p = CrawlerProcess({
# "DOWNLOADER_MIDDLEWARES": {
#     # 'scrapy_tt.middlewares.MyCustomDownloaderMiddleware': 543,
#     'scrapy_tt.middlewares.ProxyMiddleware': 100,
# }
})
p.crawl(ComSpider)
p.start()
