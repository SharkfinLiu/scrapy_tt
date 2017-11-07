# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
from scrapy import signals




# class ScrapyTtPipeline(object):
#     def process_item(self, item, spider):
#         return item

class Scrapy_findchips_dataPipeline(object):
    def __init__(self, output_file):
        self.file = codecs.open('findchips.json', 'a', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=True) + "\n"
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()

class GupiaoHkPipeline(object):
    def __init__(self):
        self.file = codecs.open("gupiao_GaoguanHk", 'a', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()

class GupiaoUsPipeline(object):
    def __init__(self):
        self.file = codecs.open("gupiao_GaoguanUS", 'a', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()


class YulePipeline(object):
    def __init__(self):
        self.file = codecs.open("Yulestar", 'a', encoding='utf-8')

    def process_item(self, item, spider):
        line = item['name']+'\t'+item['cat'] + "\n"
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()




class YuleBaikePipeline(object):
    def __init__(self,output_file):
        self.file = codecs.open(output_file, 'a', encoding='utf-8')

    def process_item(self, item, spider):
        line = item['name']+'asd'+"\n"
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()

    @classmethod
    def from_crawler(cls, crawler):
        output_file = crawler.settings.get('output_file')
        # if not output_file:
        #     output_file = "list_result" if crawler.spider.name == "sina_list" else "detail_result"

        pipeline = cls(output_file=output_file)
        crawler.signals.connect(pipeline.spider_closed, signal=signals.spider_closed)
        return pipeline


class ChuangyeComPipeline(object):
    def __init__(self):
        self.file = codecs.open("chuangye_com", 'a', encoding='utf-8')

    def process_item(self, item, spider):
        line = item['all_name']+'\t'+item['name']+'\t'+item['lever']+'\t'+item['fie']+'\t'+item['time'] + "\n"
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()


class TouzijigouPipeline(object):
    def __init__(self):
        self.file = codecs.open("touzijigou", 'a', encoding='utf-8')

    def process_item(self, item, spider):
        line = item['name']+'\t'+item['time']+'\t'+item['fav']+'\t'+item['fie'] + "\n"
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()


class TouzirenPipeline(object):
    def __init__(self):
        self.file = codecs.open("touziren", 'a', encoding='utf-8')

    def process_item(self, item, spider):
        line = item['name']+'\t'+item['company']+'\t'+item['position']+'\t'+item['fie'] + "\n"
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()

class ChengyuPipeline(object):
    def __init__(self):
        self.file = codecs.open("chengyu", 'a', encoding='utf-8')

    def process_item(self, item, spider):
        line = item['chengyu'] + "\n"
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()

