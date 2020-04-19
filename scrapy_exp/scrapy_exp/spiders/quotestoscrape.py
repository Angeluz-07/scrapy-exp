import scrapy

# ItemLoader is required to call custom Items
from scrapy.loader import ItemLoader
from scrapy_exp.items import QuotesItem


class QuotesToScrapeSpider(scrapy.Spider):
    """
    Scrapes quotes from 'quotes.toscrape.com' with the content of the quote,
    the author and the tags separated by a semi-colon.

    This spider is a good example of :
        - Scraping with pagination
        - Use of ItemLoader and Custom Item in Scrapy
        - Use of I/O processors in Custom Items
    """
    name = 'quotes'
    start_urls = [
        'https://quotes.toscrape.com/page/1/',
    ]

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
            yield scrapy.Request(url=next_page_url, callback=self.parse)
