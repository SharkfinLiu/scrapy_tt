# -*- coding: utf-8 -*-
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.utils.url import urljoin_rfc
from scrapy.http import Request
from datacrawler.items import bbsItem


class bbsSpider(BaseSpider):
    name = "bbs"
    allowed_domains = ["bbs.nju.edu.cn"]
    start_urls = ["http://bbs.nju.edu.cn/bbstop10"]

    def parseContent(self, content):
        # content = content.encode('utf8')

        authorIndex = content.index(unicode('信区', 'gbk'))
        author = content[4:authorIndex - 2]
        boardIndex = content.index(unicode('标  题', 'gbk'))
        board = content[authorIndex + 4:boardIndex - 2]
        timeIndex = content.index(unicode('南京大学小百合站 (', 'gbk'))
        time = content[timeIndex + 10:timeIndex + 34]
        content = content[timeIndex + 38:]
        return (author, board, time, content)

    def parse2(self, response):
        hxs = HtmlXPathSelector(response)
        item = response.meta['item']
        items = []

        content = hxs.select('/html/body/center/table[1]//tr[2]/td/textarea/text()').extract()[0]
        parseTuple = self.parseContent(content)
        item['author'] = parseTuple[0]
        item['board'] = parseTuple[1]
        item['time'] = parseTuple[2]
        item['content'] = parseTuple[3]
        return item

    def parse(self, response):
        hxs = HtmlXPathSelector(response)

        items = []
        title = hxs.select('/html/body/center/table/tr[position()>1]/td[3]/a/text()').extract()
        url = hxs.select('/html/body/center/table/tr[position()>1]/td[3]/a/@href').extract()
        for i in range(0, 10):
            item = bbsItem()
            item['link'] = urljoin_rfc('http://bbs.nju.edu.cn/', url[i])
            item['title'] = title[i][:-1]
            items.append(item)
        for item in items:
            yield Request(item['link'], meta={'item': item}, callback=self.parse2)


"""
1,利用meta带item进入下一个parse
2,另一种方法，在parse中使用requests库来进行请求

"""