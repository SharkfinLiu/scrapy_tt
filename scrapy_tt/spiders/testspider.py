# -*- coding: utf-8 -*-
import scrapy

# from ..items import TestprojectItem
from scrapy_tt.items import ScrapyTtItem

class TestSpider(scrapy.Spider):

    name = 'test'
    start_urls = ['https://baike.baidu.com/item/美团网/9448278?fr=aladdin&fromid=5443665&fromtitle=美团']

    def parse(self, response):
        items =[]
        for sel in response.xpath('//div[@class="para"]'):
            name = sel.xpath('text()').extract()
            items.append(ScrapyTtItem(title=name))
        return items

        # for sel in response.xpath('//ul[@class="media-list"]/li[1]/div/h4/a//text()'):
        #     if sel:
        #         is_ha = True
                # item = SearchListItem()
                # title = response.xpath('//ul[@class="media-list"]/li[1]/div/h4/a//text()').extract()
                # item['title'] = sel.xpath('div/h4/a//text()').extract()
                # item['url'] = sel.xpath('div/h4/a/@href').extract()
                # item['abstract'] = [''.join(sel.xpath('div/p//text()').extract()).replace('\n', '').replace('\u3000', '').replace(' ', '')]
                # item['imgs'] = sel.xpath('div/a/img/@src').extract()
                # content =sel.xpath('div/h4/span/text()').extract()[0].split(' ')
                # item['media_name'] = [content[0]]
                # item['published_at'] = [content[1]+' '+content[2]]
                # item['index'] = self.index
                # self.index += 1
                # return TestprojectItem(name=title)
                # items.append(item)
                # yield item
