import scrapy


class JobsSpider(scrapy.Spider):
    name = "jobs"
    allowed_domains = ["zhipin.com"]
    start_urls = ["https://www.zhipin.com/web/geek/job?query=python&city=101120500"]

    def parse(self, response):
        with open('jobs.html', 'wb') as f:
            f.write(response.body)
