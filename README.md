# Scrapy Experiments
- `./scrapy_exp/spiders` contains specific purpose spiders.
- `./scrapy_exp/items.py` contains the input/output processing step of scrapy.
- `./scrapy_exp/settings.py` contains settings of scrapy.
- `./scraped_data` contains data gathered using specific purpose spiders.

## About spiders
- `elixircompanies.py` : scrapes descriptions of companies using Elixir programming language.

## Dependencies
- [Scrapy](https://docs.scrapy.org/en/latest/intro/install.html)

## Set new dev environment in Windows
- `mkdir .venv`
- `python -m venv .venv`
- `.venv\Scripts\activate.bat`
- `pip install -r requirements.txt`

## Examples
```
>> scrapy crawl <spider_name> -o ./scraped_data/<file_name>.json #run spider and output to json file
```
