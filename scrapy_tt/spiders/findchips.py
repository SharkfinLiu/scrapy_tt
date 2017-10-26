# -*- coding: utf-8 -*-
import scrapy
import re
import time
from scrapy_tt.items import FindchipsItem


class FindchipsSpider(scrapy.Spider):
    name = 'findchips_FindchipsSpider'
    allowed_domains = ['findchips.com']
    start_urls = ["http://www.findchips.com/"]
    item = FindchipsItem()

    custom_settings = {
        "ITEM_PIPELINES": {
            'scrapy_tt.pipelines.Scrapy_findchips_dataPipeline': 300,
        },

    }

    def parse(self, response):
        for sel in response.xpath('//ul[@id="livesearch"]/li'):
            if sel:
                self.item['title'] = ''.join(sel.xpath('a/span/@title').extract())
                yield self.item
        for sel in response.xpath('//ul[@id="liveinsight"]/li'):
            if sel:
                self.item['title'] = ''.join(sel.xpath('a/span/@title').extract())
                yield self.item
        for sel in response.xpath('//ul[@id="asia"]/li'):
            if sel:
                self.item['title'] = ''.join(sel.xpath('a/span/@title').extract())
                yield self.item
        for sel in response.xpath('//ul[@iid="china"]/li'):
            if sel:
                self.item['title'] = ''.join(sel.xpath('a/span/@title').extract())
                yield self.item
        for sel in response.xpath('//ul[@id="europe"]/li'):
            if sel:
                self.item['title'] = ''.join(sel.xpath('a/span/@title').extract())
                yield self.item
        for sel in response.xpath('//ul[@id=id="america"]/li'):
            if sel:
                self.item['title'] = ''.join(sel.xpath('a/span/@title').extract())
                yield self.item
