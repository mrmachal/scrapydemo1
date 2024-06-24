import scrapy
from ..items import BigeeItem


class BiqugeSpider(scrapy.Spider):
    name = "biquge"
    allowed_domains = ["www.bigee.cc"]
    start_urls = ["https://www.bigee.cc/xuanhuan/"]
    custom_settings = {
        'ITEM_PIPELINES': {'scrapydemo1.pipelines.BigeePipeline': 300}
    }

    def parse(self, response):
        items = BigeeItem()
        lists = response.xpath("//div[@class='item']")
        for i in lists:
            items['name'] = i.xpath(".//a/text()").get()
            items['author'] = i.xpath(".//span/text()").get()

            yield items
