# -*- coding: utf-8 -*-
import scrapy
import re
# from scrapy_sina.items import SearchListItem
# import scrapy_splash
from selenium import webdriver
from scrapy.http import HtmlResponse


class Test_Phantomjs_SearchSpider(scrapy.Spider):
    name = 'Test_Phantomjs_SearchSpider'
    allowed_domains = ['zhiweidata.com']

    def __init__(self, keyword=None, *args, **kwargs):
        super(Test_Phantomjs_SearchSpider, self).__init__(*args, **kwargs)
        # self.start_urls = ["http://s.huanqiu.com/s/?q={0}&p=1".format(keyword)]
        self.start_urls = ['http://ef.zhiweidata.com/filterEvent.do&fristType=%E5%85%A8%E9%83%A8&type=%E5%85%A8%E9%83%A8&year=&month=&page=1']
        self.index = 1
        self.driver = webdriver.PhantomJS()  # 获取浏览器对象
        self.headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
            "Connection": "keep-alive",
            "Content-Length": "72",
            "Content-Type": "application/x-www-form-urlencoded",
            "Host": "ef.zhiweidata.com",
            "Referer": "http: // ef.zhiweidata.com / ",
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:55.0) Gecko/20100101 Firefox/55.0",
            "X-Requested-With": "	XMLHttpRequest",

        }
        self.cookies = {
            "Cookie": "Hm_lvt_2ed01d2d0278f62aa71273d3e3eb52b4=1506655129,1506655529,1506655534,1506656611; Hm_lpvt_2ed01d2d0278f62aa71273d3e3eb52b4= 1506665316;eventsMuseum = B15290E2516D110334607089A9CC1F8A",
        }
    # def get_next_url(self, OldUrl):
    #     l = OldUrl.split('=')
    #     OldID = int(l[2])
    #     NewID = OldID + 1
    #     NewUrl = l[0] + '=' + l[1] + '=' + str(NewID)
    #     return str(NewUrl)
    def start_requests(self):
        yield scrapy.Request(self.start_urls[0],callback=self.parse)
    def parse(self, response):
        r = response.url
        # self.driver.get("http://ef.zhiweidata.com/#!/down&fristType=%E5%85%A8%E9%83%A8&type=%E5%85%A8%E9%83%A8&year=&month=&page=1")
        # content = self.driver.page_source.encode('utf-8')
        # response = HtmlResponse(response.url, encoding='utf-8', body=content)
        print("123456")
        pass
        # for sel in response.xpath('//ul[@class="spread"]/li'):
        #     item = SearchListItem()
        #     item['title'] = ''.join(sel.xpath('dl/dd/h3/a//text()').extract())
        #     item['url'] = sel.xpath('dl/dd/h3/a/@href').extract()
        #     item['abstract'] = ''.join(sel.xpath('dl/dd/p//text()').extract()).replace('\n', '')
        #     published_at = ''.join(sel.xpath('dl/dd/span/text()').extract())
        #     p_published_at = re.compile(r'[0-9]{4}-[0-9]{2}-[0-9]{2}')
        #     if p_published_at.search(published_at):
        #         item['published_at'] = p_published_at.search(published_at).group()
        #     item['index'] = self.index
        #     self.index += 1
        #     yield item
        # for page_div in response.xpath('//div[@id="pages"]/a'):
        #     if ''.join(page_div.xpath('text()').extract()) == '下一页':
        #         next_Url = self.get_next_url(response.url)
        #         yield scrapy.Request(next_Url, callback=self.parse, dont_filter=True)
        #         break
        # else:
        #     self.driver.quit()