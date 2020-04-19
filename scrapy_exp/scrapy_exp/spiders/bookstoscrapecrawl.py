# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BookstoscrapecrawlSpider(CrawlSpider):
    """
    Scrapes title and price of books, by following links
    in the directory of the page.

    In crawl spiders don't use 'parse' as callback function name. CrawlSpider
    use that name internally.

    This spider is a good example of :
        - Crawling with pagination
        - Use of CrawlSpider
    """
    name = 'bookscrawl'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    # With LinkExtractor we only need to locate the html tag
    # containing the link(s), LinkExtractor will get the value.
    #
    # Order of rules matter?
    rules = (
        Rule(
            LinkExtractor(restrict_xpaths="//article[@class='product_pod']/div/a"),  # Where to get the links to follow
            callback='parse_item',  # Name of callback function
            follow=True  # If follow the links(make a request to them) or not
        ),
        Rule(
            LinkExtractor(restrict_xpaths="//li[@class='next']/a"),
            follow=True  # We don't specify a callback in this rule as we only use one callback and is being called in the first rule
        ),
    )

    def parse_item(self, response):
        yield {
            'title': response.xpath("//div[@class='col-sm-6 product_main']/h1/text()").get(),
            'price': response.xpath("(//div[@class='col-sm-6 product_main']/p)[1]/text()").get()
        }
