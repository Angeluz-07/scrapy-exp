# Scrapy Experiments 
Scrapy experiments with some spices of ML on the scraped data.

- `./scrapy_exp/spiders` contains specific purpose spiders.
- `./scrapy_exp/items.py` contains the input/output processing step of scrapy.
- `./scrapy_exp/settings.py` contains settings of scrapy.
- `./scraped_data` contains data gathered using specific purpose spiders.
- `./ml_iterations` contains iterations of python pre-proccesing && some ML algorithms applied to the data gathered.

## About spiders
- `elixircompanies.py` : scrapes descriptions of companies using Elixir programming language. 
  - `./ml_iterations/tm_2.py` runs topic modelling on this descriptions.

## Dependencies
- [Scrapy](https://docs.scrapy.org/en/latest/intro/install.html) (use it with virtualenv)
- [NLTK](https://www.nltk.org/install.html)
  - Specific downloaded [data](https://www.nltk.org/data.html) from NLTK servers are: punkt, stop_words, wordnet.
- [Gensim](https://radimrehurek.com/gensim/install.html)

## Examples
```
>> scrapy crawl <spider_name> -o <file_name>.json #run spider and output to json file
>> python3 ./ml_iterations/tm_2.py #run topic modelling on elixircompanies.json
```
