import scrapy
import base64
import json
from scrapy_splash import SplashRequest

FILECOUNTER = 1

class YouzhangSpider(scrapy.Spider):
    name = "youzhang"
    start_urls = [
        'https://www.youzhan.org/',
    ]

    lua_script  = '''
    function main(splash, args)
        assert(splash:go(args.url))
        assert(splash:wait(2))
        json = require('json')
        result = {}
        result.image_bytes = splash:png()
        return json.encode(result) 
    end
    '''
    def parse(self, response):
        links_xpath = "//div[@class='col-md-6 mb-8']/div/a/@href"
        for link in response.xpath(links_xpath):
            yield SplashRequest(
                url =link.get(), 
                callback = self.save_screenshot, 
                endpoint = 'execute',
                args = {
                    'lua_source' : self.lua_script
                }
            )
        """
        next_page_xpath = "//li[@class='page-item  active ']/following-sibling::li[1]/a/@href"
        next_page = response.xpath(next_page_xpath).get()
        if next_page:
            next_page = response.urljoin(next_page)
            yield scrapy.Request( url = next_page, callback = self.parse )
        """

    def save_screenshot(self, response):        
        json_string_decoded = response.body.decode("utf-8")
        response_json = json.loads(json_string_decoded)
        img_bytes = base64.b64decode(response_json['image_bytes'])

        global FILECOUNTER
        filename = f'wss_{FILECOUNTER}.png'
        with open(filename,'wb') as f :
            f.write(img_bytes)

        FILECOUNTER+=1