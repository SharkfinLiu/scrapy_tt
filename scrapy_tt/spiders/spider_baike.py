# -*- coding: utf-8 -*-
import scrapy
from scrapy_tt.items import ScrapyTtItem
from scrapy.selector import Selector
from selenium import webdriver
from scrapy.http import HtmlResponse

class SpiderBaikeSpider(scrapy.Spider):
    name = 'dmoz'
    allowed_domains = []
    start_urls = ['http://ngzb.gxrb.com.cn/html/2017-09/24/content_1434974.htm']

    # def start_requests(self):
    #     yield scrapy.Request(self.start_urls,callback=self.parse, meta={'proxy': "http://113.251.223.72:8123"})

    def parse(self, response):

        r = response.xpath('//div[@id="right_news3"]/table[2]/tr[1]/td/table/tbody/tr/td/span[2]/font/h1/text()').extract()
        # driver = webdriver.PhantomJS()
        # driver.get(response.url)
        # # json_a = driver
        # content = driver.page_source.encode('utf-8')
        # response = HtmlResponse(response.url, encoding='utf-8', body=content)
        # filename = response.url.split("/")[-2] + '.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # for sel in response.xpath('/html/body/div[5]/div/section[3]/div/div/div'):
        #     item = ScrapyTtItem()
        #     item['site_title'] = sel.xpath('/div[3]/a/div/text()').extract()
        #     item['site_descr'] = sel.xpath('/div[3]/div/text()').extract()
        #     item['link'] = sel.xpath('/div[3]/a@href').extract()
        #     yield item
        # for sel in response.xpath('//div[@class="title-and-desc"]'):
        #     item = ScrapyTtItem()
        #     # item['site_title'] = sel.xpath('a/div[@class="site-title"]/text()').extract()
        #     # item['link'] = sel.xpath('a/@href').extract()
        #     # item['site_desc'] = sel.xpath('div[@class="site-descr "]/text()').extract()
        #     yield item

        """
        <td class="ip">
        <span style="display:inline-block;">58</span>
        <span style="display:inline-block;"></span>
        <p style="display: none;"></p>
        <span></span>
        <span style="display:inline-block;">.</span>
        <span style="display:inline-block;">2</span>
        <span style="display:inline-block;">46</span>
        <div style="display:inline-block;">.</div>
        <p style="display: none;"></p>
        <span></span>
        <span style="display:inline-block;"></span>
        <p style="display: none;"></p>
        <span></span>
        <div style="display:inline-block;"></div>
        <span style="display:inline-block;">5</span>
        <p style="display: none;"></p>
        <span></span>
        <p style="display: none;">9.</p>
        <span>9.</span>
        <p style="display: none;"></p>
        <span></span>
        <span style="display:inline-block;">5</span>
        <span style="display:inline-block;">9</span>
        :
        <span class="port GEGEA">8080</span>
        </td>
        """
        # response = HtmlResponse(response.url, encoding='utf-8', body=content)
        pass