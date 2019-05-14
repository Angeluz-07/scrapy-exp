import scrapy

# Task - Section 3 - Web scraping course

#to call items
from scrapy.loader import ItemLoader 
from scrapy_exp.items import QuotesItem

class QuotesToScrapeSpider(scrapy.Spider):
	#identity
	name = "quotes"

	#requests
	start_urls = [
		'https://quotes.toscrape.com/page/1/',
	]	
	
	def parse(self,response):
		#target each box that contains info about a quote
		for quote in response.xpath("//div[@class='quote']"):
			loader = ItemLoader(item = QuotesItem(), selector = quote, response = response)
			loader.add_xpath('quote',".//span[@class='text']/text()")
			loader.add_xpath('author',".//span/small[@class='author']/text()")
			loader.add_xpath('tags',".//div[@class='tags']/a")
			yield loader.load_item()

		#from this method going recursively trough all pages.
		next_page = response.xpath("//li[@class='next']/a/@href").extract_first()
		if next_page is not None:
			next_page_link = response.urljoin(next_page)
			yield scrapy.Request(url = next_page_link, callback=self.parse)


