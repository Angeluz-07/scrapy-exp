# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

#check out docs to see for what scrapy does use i/o processors
from scrapy.loader.processors import MapCompose, TakeFirst, Join

#import useful functions to process input
from w3lib.html import remove_tags,replace_escape_chars

#custom function to remove scape chars
#modify the original just a bit to get cleaner ouput.
def remove_escape_chars(s):
    return replace_escape_chars(s,replace_by = u' ')

class CompanyItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field(
        input_processor = MapCompose(remove_tags,str.strip),
        output_processor = TakeFirst()
    )
    description= scrapy.Field(
        input_processor = MapCompose(remove_tags,remove_escape_chars,str.strip),
        output_processor = TakeFirst()
    )

class ScrapyExpItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
