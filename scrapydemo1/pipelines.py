from itemadapter import ItemAdapter
import json


class BigeePipeline(object):
    def process_item(self, item, spider):
        print(item)
        return item


class JobPipeline(object):
    def process_item(self, item, spider):
        print(item)
        return item
