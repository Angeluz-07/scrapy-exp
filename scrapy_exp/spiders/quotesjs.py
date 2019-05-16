# -*- coding: utf-8 -*-
import scrapy

# Task - Section 4 - Web scraping course
# Scraping a site wich uses js for pagination

from scrapy_splash import SplashRequest
from scrapy.selector import Selector #to query selectors on string with html content
from scrapy.loader import ItemLoader 
from scrapy_exp.items import QuotesItem

class QuotesToScrapeJsSpider(scrapy.Spider):
    name = 'quotesjs'
    allowed_domains = ['quotes.toscrape.com/js/']
    script = '''
        function main(splash, args)
          assert(splash:go(args.url))
          assert(splash:wait(0.5))
          treat = require('treat')
          result = {}
          for i = 1,9,1 do
            assert(splash:runjs('document.querySelector("li.next a").click()'))
            assert(splash:wait(1))
            result[i] = splash:html()
          end           
          return treat.as_array(result)
        end
    '''

    def start_requests(self):
        url = 'http://quotes.toscrape.com/js/'
	#this is to parse the first page
        yield SplashRequest(url = url, 
                            callback = self.parse_first_page, 
                            endpoint = 'render.html',
                            args = {'wait' : 0.5})
	#this is handle the remaining pages wich need js to be rendered
	#by default splash thinks both requests are the same, fix it by setting don_filter property
        yield SplashRequest(url = url, 
                            callback = self.parse_remaining_pages, 
                            endpoint = 'execute',
                            args = {'wait' : 0.5, 'lua_source' : self.script},
                            dont_filter = True)
	
    def parse_first_page(self, response):
        #target each box that contains info about a quote
        for quote in response.xpath("//div[@class='quote']"):
            loader = ItemLoader(item = QuotesItem(), selector = quote, response = response)
            loader.add_xpath('quote',".//span[@class='text']/text()")
            loader.add_xpath('author',".//span/small[@class='author']/text()")
            loader.add_xpath('tags',".//div[@class='tags']/a")
            yield loader.load_item()

    def parse_remaining_pages(self, response):
        #pages returned here, are strings with html content
        for page in response.data:
            sel = Selector(text = page)
             #target each box that contains info about a quote
            for quote in sel.xpath("//div[@class='quote']"):
                loader = ItemLoader(item = QuotesItem(), selector = quote, response = response)
                loader.add_xpath('quote',".//span[@class='text']/text()")
                loader.add_xpath('author',".//span/small[@class='author']/text()")
                loader.add_xpath('tags',".//div[@class='tags']/a")
                yield loader.load_item()      
