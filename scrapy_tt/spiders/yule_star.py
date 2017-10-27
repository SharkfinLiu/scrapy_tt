import scrapy
import re
import urllib.parse as up
from scrapy_tt.items import *


class YuleSpider(scrapy.Spider):
    name = 'yule_star_YuleSpider'
    custom_settings = {
        "ITEM_PIPELINES": {
            'scrapy_tt.pipelines.YulePipeline': 300,
        },
        # "output_file": name
    }

    def __init__(self, *args, **kwargs):
        super(YuleSpider, self).__init__(*args, **kwargs)
        self.start_urls = [
            "http://tieba.baidu.com/f/fdir?fd=%D3%E9%C0%D6%C3%F7%D0%C7&sd=%B8%DB%CC%A8%B6%AB%C4%CF%D1%C7%C3%F7%D0%C7&pn=1"]
        self.cat = ['港台东南亚明星',
                    '内地明星',
                    '时尚人物',
                    '主持人',
                    '其他娱乐明星',
                    '导演',
                    '戏曲曲艺明星',
                    '音乐制作人',
                    '网络名人', ]
        self.count = 0
        self.re_url_page = re.compile(r'pn=(\d{1,3})')

    def parse(self, response):
        is_not_num = 0
        is_has = True
        for sels in response.xpath('//div[@class="sub_dir_box"]/table/tr'):
            for sel in sels.xpath('td'):
                if ''.join(sel.xpath('a/text()').extract()) == '':
                    is_not_num += 1
                    if is_not_num >100:
                        is_has = False
                    continue
                item = YulestarItem()
                item['name'] = ''.join(sel.xpath('a/text()').extract())
                item['cat'] = self.cat[self.count]
                yield item
            if is_has:
                pass
            else:
                break
        if is_has:
            cate = up.quote(self.cat[self.count].encode('gbk'))
            page_num = int(self.re_url_page.search(response.url).group(1)) + 1
            new_url = "http://tieba.baidu.com/f/fdir?fd=%D3%E9%C0%D6%C3%F7%D0%C7&sd=" + str(cate) + "&pn=" + str(page_num)
            yield scrapy.Request(new_url,self.parse,dont_filter=True)
        else:
            self.count += 1
            if self.count < 9:
                cate = up.quote(self.cat[self.count].encode('gbk'))
                new_url = "http://tieba.baidu.com/f/fdir?fd=%D3%E9%C0%D6%C3%F7%D0%C7&sd=" + str(cate) + "&pn=1"
                yield scrapy.Request(new_url, self.parse, dont_filter=True)
            else:
                return
