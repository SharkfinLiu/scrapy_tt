import scrapy


class SpiderName(scrapy.Spider):
    name = "some_spider"

    def parse(self, response):
        pass

    def modify_realtime_request(self, request):
        request.meta["dont_redirect"] = True
        return request
