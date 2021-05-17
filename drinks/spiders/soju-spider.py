import scrapy 
from scrapy.loader import ItemLoader

class SojuSpider(scrapy.Spider):
    name="soju"

    start_urls = ["https://www.lcbo.com/webapp/wcs/stores/servlet/en/lcbo/spirits-15/shochu-soju-15017"]

    def parse(self, response):
        drinks = response.css('.product')
        for drink in drinks:
            yield {
                'name': ".product_name a::text",
                'price': "#content .price::text",
                'link': 

            }