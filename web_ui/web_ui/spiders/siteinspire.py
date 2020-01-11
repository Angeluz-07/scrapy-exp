# -*- coding: utf-8 -*-
import scrapy


class SiteinspireSpider(scrapy.Spider):
    name = 'siteinspire'
    allowed_domains = ['siteinspire.com/websites']
    start_urls = ['http://siteinspire.com/websites/']
    
    def parse(self, response):
        links_xpath = "//div[@class='overlay']/a/@href"
        for link in response.xpath(links_xpath):
            yield {
                'url' : link.get()
            }
        
        next_page_xpath = "//div[@class='pagination pagination-centered']/ul/li[@class='active']/following-sibling::li[1]/a/@href"
        next_page = response.xpath(next_page_xpath).get()
        if next_page:
            next_page = response.urljoin(next_page)
            yield scrapy.Request( url = next_page, callback = self.parse, dont_filter=True)
        
