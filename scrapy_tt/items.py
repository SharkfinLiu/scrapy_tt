# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyTtItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    site_title = scrapy.Field()
    site_desc = scrapy.Field()
    link = scrapy.Field()


class FindchipsItem(scrapy.Item):
    title = scrapy.Field()
    elementnumber = scrapy.Field()


class GupiaoItem(scrapy.Item):
    name = scrapy.Field()
    jobs = scrapy.Field()
    age_sex = scrapy.Field()
    des = scrapy.Field()
    com_name = scrapy.Field()


class YulestarItem(scrapy.Item):
    name = scrapy.Field()
    cat = scrapy.Field()


class ChuangyeItem(scrapy.Item):
    name = scrapy.Field()
    lever = scrapy.Field()
    fie = scrapy.Field()
    time = scrapy.Field()
    all_name =scrapy.Field()

class TouzijigouItem(scrapy.Item):
    name = scrapy.Field()
    fav = scrapy.Field()
    fie = scrapy.Field()
    time = scrapy.Field()

class TouzirenItem(scrapy.Item):
    name = scrapy.Field()
    position = scrapy.Field()
    fie = scrapy.Field()
    company = scrapy.Field()