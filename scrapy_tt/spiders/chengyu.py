import scrapy
import re
from scrapy_tt.items import *
import requests
from scrapy.http import HtmlResponse


class ChengyuSpider(scrapy.Spider):
    name = 'chengyu_ChengyuSpider'
    custom_settings = {
        "ITEM_PIPELINES": {
            'scrapy_tt.pipelines.ChengyuPipeline': 300,
        },
        # "output_file": name
    }

    def __init__(self, *args, **kwargs):
        super(ChengyuSpider, self).__init__(*args, **kwargs)
        self.start_urls = ["http://www.guoxue.com/chengyu/cys_001.htm"]
        # self.re_page = re.compile(r'cys_0(\d{1,3})')
        self.count = 1

    def parse(self, response):
        for sel in response.xpath('//span[@style="font-size: 12pt"]'):
            if sel:
                item = ChengyuItem()
                item['chengyu'] = ''.join(sel.xpath('text()').extract()).replace('】', '').replace('【', '')
                yield item
        self.count += 1
        if self.count < 10:
            new_url = "http://www.guoxue.com/chengyu/cys_00" + str(self.count) + ".htm"
            yield scrapy.Request(new_url, self.parse, dont_filter=True)
        elif 10 <= self.count < 25:
            new_url = "http://www.guoxue.com/chengyu/cys_0" + str(self.count) + ".htm"
            yield scrapy.Request(new_url, self.parse, dont_filter=True)
        else:
            return
