# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy_splash import SplashRequest


class UiSaverSpider(scrapy.Spider):
    """
    Opens a json file with urls previously scraped, makes a request
    to each url and takes a screenshot of the website rendered.

    Parameters:
        file_counter : auto incremental value to use in the name of the image saved.
        source_site  : name of the site where urls were obtained, used to name the image saved.
        path_to_urls : relative path to the file with urls to use.
        n_sites : how many sites to scrape from the total available in the file with urls.

    Requires a running Splash server. Also other configurations, check out
    'https://github.com/scrapy-plugins/scrapy-splash#configuration'
    """
    name = 'ui_saver'
    file_counter = 0
    source_site = 'youzhan'
    path_to_urls = f'./data/youzhan_urls.json'
    n_sites = 10

    def start_requests(self):
        # From results of youzhan spider
        with open(self.path_to_urls, 'r') as json_file:
            urls = json.load(json_file)

        N = self.n_sites
        for obj in urls[:N]:
            yield SplashRequest(
                url=obj['url'],
                callback=self.save_screenshot,
                endpoint='render.png',
                args={
                    'wait': 5  # seconds to wait for page to be rendered
                }
            )

    def save_screenshot(self, response):
        """
        From scrapy_splash docs. As we use endpoint 'render.png', a binary
        response will be returned in the in a SplashReponse object.

        We can access to image in bytes from response.body and the url hitted
        from response.url .
        """

        img_in_bytes = response.body
        filename = f'./data/{self.source_site}_{self.file_counter}.png'
        with open(filename, 'wb') as f:
            f.write(img_in_bytes)

        self.file_counter += 1
        self.logger.info(f'File counter {self.file_counter}')
        self.logger.info(f'Web UI saved from {response.url}')
