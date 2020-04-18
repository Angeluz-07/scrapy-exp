# Scrapy Experiments
- `./scrapy_exp/spiders` contains specific purpose spiders.
- `./scrapy_exp/items.py` contains the input/output processing step of scrapy.
- `./scrapy_exp/settings.py` contains settings of scrapy.
- `./scraped_data` contains data gathered using specific purpose spiders.

## About spiders
- `elixircompanies.py` : scrapes descriptions of companies using Elixir programming language.

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
## Examples
```
scrapy crawl <spider_name> -o ./scraped_data/<file_name>.json #run spider and output to json file
```

### Web UI scraping

In the project folder `/web_ui` is possible to run
```
scrapy crawl youzhan -o ./data/<output_filename>.json
scrapy crawl siteinspire -o ./data/<output_filename>.json
```
These spiders scrape website urls. Checkout spiders for more details.


## Run scrapy with Splash

Check [Splash Docs](https://splash.readthedocs.io/en/stable/) for installation instructions.

In a new a terminal run
```
sudo docker run -it -p 8050:8050 --rm scrapinghub/splash
```


## Built with
- [Scrapy](https://docs.scrapy.org/en/latest/intro/install.html)
- [Splash](https://splash.readthedocs.io/en/stable/)
