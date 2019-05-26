# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem

#this is for quotestoscrapecrawl spider
class FilterDuplicate(object):
    seen = None

    def open_spider(self,spider):
        #instantiate your set here
        self.seen = set()
    
    #I got an error using item in the set. 
    #I solved by using the text instead. 
    #see ref: https://stackoverflow.com/questions/13264511/typeerror-unhashable-type-dict
    def process_item(self, item, spider):
        #check if item is already on your set
        if item.get('quote') in self.seen:
            raise DropItem("Item dropped {0}".format(item.get('quote')))
        else:
            #means if the item is not on your set add it
            self.seen.add(item.get('quote'))
            return item

class ScrapyExpPipeline(object):
    def process_item(self, item, spider):
        return item
