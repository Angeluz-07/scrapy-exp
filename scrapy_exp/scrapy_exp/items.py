# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

# Utilities to process input
from w3lib.html import remove_tags, replace_escape_chars
import re

# Check out Scrapy docs to see the use of I/O processors
from scrapy.loader.processors import MapCompose, TakeFirst, Join


#custom function to remove scape chars
#modify the original just a bit to get cleaner ouput.
def remove_escape_chars(s):
    return replace_escape_chars(s,replace_by = u' ')


def just_number(s):
    """
    Clean numeric values.
    It doesn't work if the number has commas and single quotes(e.g. 1'000,000)
    """
    return re.sub(r'[^\d\.]', "", s)


# Used in elixircompanies.py
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

#Used in olx_houses.py
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


class QuotesItem(scrapy.Item):
    """
    Custom Item used in ./spiders/quotestoscrape.py
    """

    def remove_quotations(s: str) -> str:
        """
        Remove  '“' and '”' characters
        """
        return s.replace(u'“', '').replace(u'”', '')

    # Item Fields
    quote = scrapy.Field(
        input_processor=MapCompose(
            str.strip,
            remove_quotations
        ),
        output_processor=TakeFirst()
    )
    author = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst()
    )
    tags = scrapy.Field(
        input_processor=MapCompose(remove_tags, str.strip),
        output_processor=Join(';')
    )


class ScrapyExpItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
