import scrapy
import time
import requests

class ImdbSpider(scrapy.Spider):
    name="movies"
    start_urls=['https://www.imdb.com/search/title/?release_date=2022-01-01,2023-12-31']
    
    def parse(self,response):
        data={}
        imdb_block=response.css("div[class='lister-item mode-advanced']")
        data["length"]=len(imdb_block)        
        for ln in imdb_block:
            data['name']=ln.css("h3[class='lister-item-header'] a::text").extract()
            data['ratings']=ln.css("div[class='inline-block ratings-imdb-rating'] strong::text").extract()
            data['releasedate']=ln.css("span[class='lister-item-year text-muted unbold']::text").extract()
            yield data