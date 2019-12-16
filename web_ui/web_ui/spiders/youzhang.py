import scrapy


class YouzhangSpider(scrapy.Spider):
    name = "youzhang"
    start_urls = [
        'https://www.youzhan.org/',
    ]

    def parse(self, response):
        links_xpath = "//div[@class='col-md-6 mb-8']/div/a/@href"
        for link in response.xpath(links_xpath):
            yield {
                'link' : link.get()
            }
        
        next_page_xpath = "//li[@class='page-item  active ']/following-sibling::li[1]/a/@href"
        next_page = response.xpath(next_page_xpath).get()
        if next_page:
            next_page = response.urljoin(next_page)
            yield scrapy.Request( url = next_page, callback = self.parse )