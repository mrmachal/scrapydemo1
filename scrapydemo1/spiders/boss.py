import scrapy
from ..items import Scrapydemo1Item


class BossSpider(scrapy.Spider):
    name = "boss"
    allowed_domains = ["zhipin.com"]
    start_urls = ["https://www.zhipin.com/web/geek/job?query=python&city=101120200"]

    def parse(self, response):
        yield response.body()
