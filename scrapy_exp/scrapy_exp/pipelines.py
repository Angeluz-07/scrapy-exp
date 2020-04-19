# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem


class FilterDuplicate(object):
    """
    Item Pipeline for QuotesItem to filter duplicates based in the content
    of the quote.
    """
    seen = None

    def open_spider(self, spider):
        # Instantiate your set here
        self.seen = set()

    # Got an error by using Item object in the set.
    # Solved by using the text instead.
    # see ref: 'https://stackoverflow.com/questions/13264511/typeerror-unhashable-type-dict'
    def process_item(self, item, spider):
        # If item in set, ignore it
        if item.get('quote') in self.seen:
            raise DropItem("Item dropped {0}".format(item.get('quote')))
        else:
            # If item not in the set, add it
            self.seen.add(item.get('quote'))
            return item


class ScrapyExpPipeline(object):
    def process_item(self, item, spider):
        return item
