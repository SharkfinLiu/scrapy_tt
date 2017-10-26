import scrapy
import json
import re
from selenium import webdriver
from scrapy.http import HtmlResponse

# class ItjuziSearchSpider(scrapy.Spider):
#     name = "itjuzi_ItjuziSearchSpider"
#     allowed_domains = []
#
#     def __init__(self, *args, **kwargs):
#         super(ItjuziSearchSpider, self).__init__(*args, **kwargs)
#         self.start_url = ["https://www.itjuzi.com/company?status=1&page=3"]
#         # self.re_gupiao = re.compile(r'(\d{6}),([\u4e00-\u9fa5,\w,\*]+),')
#         # self.c = 1
#         # self.count = 0
#
#     def start_requests(self):
#         yield scrapy.Request(self.start_url[0],self.parse)
#
#     def parse(self, response):
#         print('123456')
#         raw = json.loads(response.body_as_unicode())
#         # entries = self.re_gupiao.findall(response.text)
#         # if entries:
#             # for entry in entries:
#                 # print(entry)
#                 # with open('gupiao_600', mode='a+', encoding='utf-8') as f:
#                     # print(entry)
#                     # self.count += 1
#                     # f.write("{'%s':'%s'}" % (entry[0], entry[1]) + '\n')
#             # print("count:%d" % self.count)
#         # if self.c > 33 :
#         #     return
#         # self.c += 1
#         # newUrl = "http://xuanguapi.eastmoney.com/Stock/JS.aspx?type=xgq&sty=xgq&token=eastmoney&c=[gf1]&p="+ str(self.c) +"&jn=tEIlyyvs&ps=40&s=gf1&st=-1"
#         yield scrapy.Request(newUrl,self.parse,dont_filter=True)
if __name__ == "__main__":
    url = "http://www.mouser.cn/ProductDetail/Texas-Instruments/LM22670MRX-50-NOPB/?qs=X1J7HmVL2ZHMuvtk1RgCmg==&utm_source=findchips&utm_medium=aggregator&utm_campaign=LM22670MRX-50-NOPB&utm_term=LM22670MRX-50-NOPB&utm_content=Texas-Instruments"
    driver = webdriver.PhantomJS()  # 获取浏览器对象
    driver.get(url)
    content = driver.page_source.encode('utf-8')
    response = HtmlResponse(url, encoding='utf-8', body=content)
    if response.xpath('//span[@id="ctl00_ContentMain_Specifications_dlspec_ctl01_lblName"]/text()'):
        # item = ChipCatItem()/
        category = ''.join(
            response.xpath('//span[@id="ctl00_ContentMain_Specifications_dlspec_ctl01_lblName"]/text()').extract())
        # if self.re_part_no.search(response.url):
        #     item['part_no'] = self.re_part_no.search(response.url).group(1).strip()
        # yield item
    pass