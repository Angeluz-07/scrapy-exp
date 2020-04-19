import scrapy

#to call items
from scrapy.loader import ItemLoader 
from scrapy_exp.items import HouseItem

####
# Spider to scrap data info of houses for sale.
# website: https://olx.com.ec/
# In order to not hit hard the server, set DELAY variables on settings.py 

# last date scraped : 2019/04/29 
class HouseSpider(scrapy.Spider):
	#identity
	name = "olx_houses"

	#requests
	#def start_requests(self):
	#	#starting url	
	#	url = 'https://olx.com.ec/nf/departamentos-casas-venta-cat-367/-flo_casas'	
	#	yield scrapy.Request(url = url, callback=self.parse)

	# shorcut for star_requests
	start_urls = [
    'https://www.olx.com.ec/nf/departamentos-casas-venta-cat-367/-flo_casas'
	]

	# Here, you could use response.selector.xpath or response.xpath interchangeably
	# Don't clean data here, use Items on items.py instead
	def parse(self,response):
		#target each box that contains info about a company
		for house in response.xpath("//ul[@class='items-list ']/li"):
			#I don't see the point of using ItemLoader yet
			loader = ItemLoader(item = HouseItem(), selector = house, response = response)
			loader.add_xpath('title',".//div/a[1]/@title")#check
			loader.add_xpath('price',".//p[@class='items-price']/a/text()[1]")
			loader.add_xpath('surface',".//span[starts-with(@class,'optional surface')][1]/text()")			
			loader.add_xpath('bedrooms',".//span[starts-with(@class,'optional bedrooms')]")		
			loader.add_xpath('bathrooms',".//span[starts-with(@class,'optional bathrooms')]")					
			yield loader.load_item()

	
		#from this method going recursively trough all pages.
		next_page = response.xpath("//a[@class='pagination-button next']/@href").extract_first()
		if next_page:
			next_page_link = response.urljoin(next_page)
			yield scrapy.Request(url = next_page_link, callback=self.parse)

