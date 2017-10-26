# -*- coding: utf-8 -*-
import requests
from selenium import webdriver
from scrapy.http import HtmlResponse
# r = requests.post("http://ef.zhiweidata.com/#!/down&fristType=%E5%85%A8%E9%83%A8&type=%E5%85%A8%E9%83%A8&year=&month=&page=1")
#
# # r.xpath('//td[@class=".aa"//text()').extract()
# print("123456")
# pass

driver = webdriver.PhantomJS()  # 获取浏览器对象
driver.get("http://ef.zhiweidata.com/#!/down")
a = driver.current_url
content = driver.page_source.encode('utf-8')
response = HtmlResponse(a, encoding='utf-8', body=content)
print("qqqqqqqqqqq")