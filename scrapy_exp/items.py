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
import re

#custom function to remove scape chars
#modify the original just a bit to get cleaner ouput.
def remove_escape_chars(s):
    return replace_escape_chars(s,replace_by = u' ')

#clean numeric values. 
#It doesn't work if the number has commas and single quotes(e.g. 1'000,000)
def just_number(s):
    return re.sub("[^\d\.]","",s)

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

class HouseItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field(
	input_processor = MapCompose(str.strip),
        output_processor = TakeFirst()
    )
    price = scrapy.Field(
	input_processor = MapCompose(just_number,str.strip),
        output_processor = TakeFirst()
    ) 
    surface = scrapy.Field(
	input_processor = MapCompose(just_number,str.strip),
        output_processor = TakeFirst()
    )
    bedrooms = scrapy.Field(
        input_processor = MapCompose(remove_tags,str.strip),
        output_processor = TakeFirst()
    )    
    bathrooms =  scrapy.Field(
        input_processor = MapCompose(remove_tags,str.strip),
        output_processor = TakeFirst()
    )    
class ScrapyExpItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
