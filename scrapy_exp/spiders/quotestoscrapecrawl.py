# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


# Task - Section 7 - Web scraping course

class QuotesToScrapeCrawlSpider(CrawlSpider):
    name = 'quotestoscrapecrawl'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    #In this case we just locate the html tag with the link and the LinkExtractor object will extract the link
    rules = (
        Rule(LinkExtractor(restrict_xpaths="//span[@class='tag-item']/a"), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths="//li[@class='next']/a"), callback='parse_item', follow=True),
    )

    #for this assignment was required just to extract the text
    def parse_item(self, response):
        #target each box that contains info about a quote
        for quote in response.xpath("//div[@class='quote']"):
            yield {
                'quote' : quote.xpath(".//span[@class='text']/text()").extract_first()
            }       
