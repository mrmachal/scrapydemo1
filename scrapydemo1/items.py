# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BigeeItem(scrapy.Item):
    name = scrapy.Field()
    author = scrapy.Field()


class JobItem(scrapy.Item):
    job_title = scrapy.Field()
    job_corporation = scrapy.Field()
    job_salary = scrapy.Field()
