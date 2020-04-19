# Scrapy Experiments

A personal repository with Scrapy projects for learning and experimentation purposes.

## Set development environment
###  Windows
```
mkdir .venv
python -m venv .venv
.venv\Scripts\activate.bat
pip install -r requirements.txt
```
###  Linux Based OS
```
mkdir .venv
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
````
## Projects

### Scrapy examples 

Contains examples of how to create spiders for basic webscraping.

In the project folder `/scrapy_exp` is possible to run.
```
scrapy crawl quotes -o ./data/<output_filename>.json
scrapy crawl quotesjs -o ./data/<output_filename>.json
scrapy crawl bookscrawl -o ./data/<output_filename>.json
```

### Web UI scraping

Contains spiders to scrape urls and take screenshots of websites.

In the project folder `/web_ui` is possible to run.
```
scrapy crawl youzhan -o ./data/<output_filename>.json
scrapy crawl siteinspire -o ./data/<output_filename>.json
scrapy crawl ui_saver
```

Output to xml and csv formats is also available, by changing output file format from `.json` to `.xml` or `.csv`.

These spiders scrape website urls. Checkout spiders for more details.


## Run scrapy with Splash

Some spiders require Splash. In a new a terminal run.
```
sudo docker run -it -p 8050:8050 --rm scrapinghub/splash
```

Check [Splash Docs](https://splash.readthedocs.io/en/stable/) for installation instructions.


## Built with
- [Scrapy](https://docs.scrapy.org/en/latest/intro/install.html)
- [Splash](https://splash.readthedocs.io/en/stable/)
