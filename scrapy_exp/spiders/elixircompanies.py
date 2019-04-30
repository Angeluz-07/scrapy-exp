import scrapy

#to call items
from scrapy.loader import ItemLoader 
from scrapy_exp.items import CompanyItem

####
# Spider to scrap data info of companies using Elixir programming language.
# website: https://elixir-companies.com/
# In order to not hit hard the server, set DELAY variables on settings.py 

# last date scraped : 2019/04/29 
class CompanySpider(scrapy.Spider):
	#identity
	name = "elixircompanies"

	#requests
	#def start_requests(self):
	#	#starting url	
	#	url = 'https://elixir-companies.com/en/browse?page=1'		
	#	yield scrapy.Request(url = url, callback=self.parse)

	# shorcut for star_requests
	start_urls = [
		'https://elixir-companies.com/en/browse?page=1'
	]

	# Here, you could use response.selector.xpath or response.xpath interchangeably
	# Don't clean data here, use Items on items.py instead
	def parse(self,response):
		#target each box that contains info about a company
		for company in response.xpath("//div[@class='company box ']"):
			#I don't see the point of using ItemLoader yet
			loader = ItemLoader(item = CompanyItem(), selector = company, response = response)
			loader.add_xpath('name',".//p[@class='title is-4 thin']")		
			loader.add_xpath('description',".//div[@class='content company-description is-size-7 has-text-centered']")
			yield loader.load_item()

"""		
		#from this method going recursively trough all pages.
		next_page = response.xpath("//ul[@class='pagination-list']/li[last()]/a/@href").extract_first()
		if next_page:
			next_page_link = response.urljoin(next_page)
			yield scrapy.Request(url = next_page_link, callback=self.parse)
"""
