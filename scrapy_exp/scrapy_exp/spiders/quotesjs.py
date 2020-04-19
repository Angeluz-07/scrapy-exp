# -*- coding: utf-8 -*-
import scrapy

from scrapy_splash import SplashRequest
from scrapy.loader import ItemLoader
from scrapy_exp.items import QuotesItem


class QuotesToScrapeJsSpider(scrapy.Spider):
    """
    Scrapes quotes from 'quotes.toscrape.com/js' with the content of the quote,
    the author and the tags separated by a semi-colon. This page requires
    the use of splash as it loads its content using js.

    This spider is a good example of :
        - Use of Scraping with Splash
        - Use of Lua script for Splash

    Requires a running Splash server. Also other configurations, check out
    'https://github.com/scrapy-plugins/scrapy-splash#configuration'
    """
    name = 'quotesjs'
    allowed_domains = ['quotes.toscrape.com']
    script = '''
        function main(splash, args)
          assert(splash:go(args.url))
          assert(splash:wait(5))
          return splash:html()
        end
    '''

    def start_requests(self):
        url = 'http://quotes.toscrape.com/js/'
        yield SplashRequest(
            url=url,
            callback=self.parse,
            endpoint='execute',
            args={
                'lua_source': self.script  # Arguments to Splash 'execute' endpoint. Check Splash docs.
            }
        )

    def parse(self, response):
        # Iterate over all boxes that contain info about a quote
        for quote_div in response.xpath("//div[@class='quote']"):
            loader = ItemLoader(
                item=QuotesItem(),  # Custom Item to populate
                selector=quote_div,  # Selector object to extract data from
            )
            loader.add_xpath('quote', ".//span[@class='text']/text()")
            loader.add_xpath('author', ".//span/small[@class='author']/text()")
            loader.add_xpath('tags', ".//div[@class='tags']/a")
            yield loader.load_item()

        # With the following code we go trough all pages.
        next_page_xpath = "//li[@class='next']/a/@href"
        next_page = response.xpath(next_page_xpath).get()
        if next_page:
            next_page_url = response.urljoin(next_page)
            yield SplashRequest(
                url=next_page_url,
                callback=self.parse,
                endpoint='execute',
                args={
                    'lua_source': self.script_  # Arguments to Splash 'execute' endpoint. Check Splash docs.
                }
            )
