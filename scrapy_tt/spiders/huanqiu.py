# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy_sina.items import SearchListItem
# import scrapy_splash
from selenium import webdriver
from scrapy.http import HtmlResponse


class HuanqiuSearchSpider(scrapy.Spider):
    name = 'huanqiu_HuanqiuSearchSpider'
    allowed_domains = ['huanqiu.com']

    def __init__(self, keyword=None, *args, **kwargs):
        super(HuanqiuSearchSpider, self).__init__(*args, **kwargs)
        self.start_urls = ["http://s.huanqiu.com/s/?q={0}&p=1".format(keyword)]
        self.index = 1
        self.driver = webdriver.PhantomJS()  # 获取浏览器对象

    def get_next_url(self, OldUrl):
        l = OldUrl.split('=')
        OldID = int(l[2])
        NewID = OldID + 1
        NewUrl = l[0] + '=' + l[1] + '=' + str(NewID)
        return str(NewUrl)

    def parse(self, response):
        self.driver.get(response.url)
        content = self.driver.page_source.encode('utf-8')
        response = HtmlResponse(response.url, encoding='utf-8', body=content)
        for sel in response.xpath('//ul[@class="spread"]/li'):
            item = SearchListItem()
            item['title'] = ''.join(sel.xpath('dl/dd/h3/a//text()').extract())
            item['url'] = sel.xpath('dl/dd/h3/a/@href').extract()
            item['abstract'] = ''.join(sel.xpath('dl/dd/p//text()').extract()).replace('\n', '')
            published_at = ''.join(sel.xpath('dl/dd/span/text()').extract())
            p_published_at = re.compile(r'[0-9]{4}-[0-9]{2}-[0-9]{2}')
            if p_published_at.search(published_at):
                item['published_at'] = p_published_at.search(published_at).group()
            item['index'] = self.index
            self.index += 1
            yield item
        for page_div in response.xpath('//div[@id="pages"]/a'):
            if ''.join(page_div.xpath('text()').extract()) == '下一页':
                next_Url = self.get_next_url(response.url)
                yield scrapy.Request(next_Url, callback=self.parse, dont_filter=True)
                break
        else:
            self.driver.quit()