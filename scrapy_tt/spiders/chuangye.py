import scrapy
import re
from scrapy_tt.items import *
import requests
from scrapy.http import HtmlResponse

class ChuangyeComSpider(scrapy.Spider):
    name = 'chuangye_ChuangyeComSpider'
    custom_settings = {
        "ITEM_PIPELINES": {
            'scrapy_tt.pipelines.ChuangyeComPipeline': 300,
        },
        # "output_file": name
    }

    def __init__(self,*args,**kwargs):
        super(ChuangyeComSpider,self).__init__(*args,**kwargs)
        self.start_urls = ["http://www.cyzone.cn/vcompany/list-0-9-1-0-0/0"]
        self.re_time = re.compile(r'(\d{4})')
        self.re_url = re.compile(r'list-\d-(\d{1,2})-(\d{1,3})')

    def parse(self, response):
        is_has = False
        for sel in response.xpath('//tr[@class="table-plate item"]'):
            if sel:
                is_has = True
                item = ChuangyeItem()
                item['time'] = ''.join(sel.xpath('td[@class="table-time"]/text()').extract())
                item['name'] = ''.join(sel.xpath('@data-title').extract())
                item['lever'] = ''.join(sel.xpath('td[@class="table-stage"]/a/text()').extract())
                item['fie'] = ''.join(sel.xpath('td[@class="table-type"]/a/text()').extract())
                item['all_name'] = ''.join(sel.xpath('td[@class="table-company-tit"]/a/@href').extract())
                r = requests.get(item['all_name'])
                r = HtmlResponse(item['all_name'], encoding='utf-8', body=r.text)
                all_name = ''.join(r.xpath('//div[@class="ti-left pull-left"]/ul/li[@class="time"]/text()').extract()).split('：')
                item['all_name'] = all_name[-1]
                if self.re_time.search(item['time']):
                    if int(self.re_time.search(item['time']).group(1)) >2006:
                        yield item
        if is_has:
            if self.re_url.search(response.url):
                page_num = int(self.re_url.search(response.url).group(2)) + 1
                type_num = self.re_url.search(response.url).group(1)
            new_url = "http://www.cyzone.cn/vcompany/list-0-"+str(type_num)+"-"+str(page_num)+"-0-0/0"
            yield scrapy.Request(new_url,self.parse,dont_filter=True)
        else:
            if self.re_url.search(response.url):
                type_num = int(self.re_url.search(response.url).group(1)) + 1
                if type_num <16:
                    new_url = "http://www.cyzone.cn/vcompany/list-0-" + str(type_num) + "-1-0-0/0"
                    yield scrapy.Request(new_url,self.parse,dont_filter=True)
                else:
                    return

class TouzijigouSpider(scrapy.Spider):

    name = 'chuangye_TouzijigouSpider'
    custom_settings = {
        "ITEM_PIPELINES": {
            'scrapy_tt.pipelines.TouzijigouPipeline': 300,
        },
        # "output_file": name
    }

    def __init__(self,*args,**kwargs):
        super(TouzijigouSpider,self).__init__(*args,**kwargs)
        self.start_urls = ["http://www.cyzone.cn/company/list-0-1-4/"]
        self.re_url = re.compile(r'list-\d-(\d{1,3})')

    def parse(self, response):
        is_has = False
        for sel in response.xpath('//tr[@class="table-plate2"]'):
            if sel:
                is_has = True
                item = TouzijigouItem()
                item['time'] = ''.join(sel.xpath('td[3]/text()').extract())
                item['name'] = ''.join(sel.xpath('td[@class="table-follow"]/a/@data-title').extract())
                item['fav'] = ','.join(sel.xpath('td[5]/text()').extract())
                item['fie'] = re.sub('\s','',','.join(sel.xpath('td[6]/text()').extract()))
                yield item
        if is_has:
            if self.re_url.search(response.url):
                page_num = int(self.re_url.search(response.url).group(1)) + 1
            new_url = "http://www.cyzone.cn/company/list-0-"+str(page_num)+"-4/"
            yield scrapy.Request(new_url,self.parse,dont_filter=True)


class TouzirenSpider(scrapy.Spider):

    name = 'chuangye_TouzirenSpider'
    custom_settings = {
        "ITEM_PIPELINES": {
            'scrapy_tt.pipelines.TouzirenPipeline': 300,
        },
        # "output_file": name
    }

    def __init__(self, *args, **kwargs):
        super(TouzirenSpider, self).__init__(*args, **kwargs)
        self.start_urls = ["http://www.cyzone.cn/people/list-0-1-0-0/"]
        self.re_url = re.compile(r'list-\d-(\d{1,3})')

    def parse(self, response):
        is_has = False
        for sel in response.xpath('//tr[@class="ltp-plate"]'):
            if sel:
                is_has = True
                item = TouzirenItem()
                item['position'] = ''.join(sel.xpath('td[4]/text()').extract())
                item['name'] = ''.join(sel.xpath('td[@class="people-name"]/a/text()').extract())
                item['company'] = ','.join(sel.xpath('td[3]/a/text()').extract())
                item['fie'] = re.sub('\s+',',',''.join(sel.xpath('td[5]//text()').extract()).strip())
                yield item
        if is_has:
            if self.re_url.search(response.url):
                page_num = int(self.re_url.search(response.url).group(1)) + 1
            new_url = "http://www.cyzone.cn/people/list-0-" + str(page_num) + "-0-0/"
            yield scrapy.Request(new_url, self.parse, dont_filter=True)