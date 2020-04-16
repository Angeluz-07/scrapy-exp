# -*- coding: utf-8 -*-
import scrapy
import scrapy.spidermiddlewares.httperror
import base64
import json
from scrapy_splash import SplashRequest

N = 11
FILECOUNTER = 0

class UiSaverSpider(scrapy.Spider):
    name = 'ui_saver'    
    lua_script  = '''
    function main(splash, args)
        splash.resource_timeout = 10.0
        assert(splash:go(args.url))
        assert(splash:wait(5))
        json = require('json')
        result = {}
        result.image_bytes = splash:png()
        return json.encode(result) 
    end
    '''
    def start_requests(self):
        #--siteinspire
        #urls_path = f'./web_ui/scraped_data/siteinspire/batches/b_{N}/url.json'
        
        #--youzhang
        urls_path =  f'./web_ui/scraped_data/youzhang/urls.json'

        #load 100 urls
        with open(urls_path,'r') as json_file:
            data = json.load(json_file)
        
        #for each url, make splash request and save screenshot
        for elem in data:            
            url = elem['url']
            try : 
                yield SplashRequest(
                    url = url, 
                    callback = self.save_screenshot, 
                    endpoint = 'execute',
                    args = {
                        'lua_source' : self.lua_script,
                        #'wait' : 5,
                        #'resource_timeout': 15
                    }
                )
            except :
                pass
            

    def parse(self, response):
        pass

    def save_screenshot(self, response):        
        json_string_decoded = response.body.decode("utf-8")
        response_json = json.loads(json_string_decoded)
        img_bytes = base64.b64decode(response_json['image_bytes'])

        global FILECOUNTER
        #filename = f'./web_ui/scraped_data/siteinspire/batches/b_{N}/{N}_wss_{FILECOUNTER}.png'
        filename = f'./web_ui/scraped_data/youzhang/images/wss_{FILECOUNTER}.png'
        with open(filename,'wb') as f :
            f.write(img_bytes)

        FILECOUNTER+=1