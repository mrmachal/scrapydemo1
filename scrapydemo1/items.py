# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Scrapydemo1Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    city = scrapy.Field()
    salary = scrapy.Field()
    degree = scrapy.Field()


class TxmoviesItem(scrapy.Item):
    name = scrapy.Field()
    description = scrapy.Field()


class BigeeItem(scrapy.Item):
    name = scrapy.Field()
    author = scrapy.Field()
