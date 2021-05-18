import scrapy 
from scrapy.loader import ItemLoader
from drinks.items import DrinksItem

class SojuSpider(scrapy.Spider):
    name="soju"

    start_urls = ["https://www.lcbo.com/webapp/wcs/stores/servlet/en/lcbo/spirits-15/shochu-soju-15017"]

    def parse(self, response):
        drinks = response.css('.product')
        for drink in drinks:
            # yield {
            #     'name': drink.css(".product_name a::text").get(),
            #     'price': drink.css("#content .price::text").get(),
            #     'link': drink.css(".product_name a::attr(href)").get()
            # }
            loader = ItemLoader(item = DrinksItem(), selector = drink)
            loader.add_css('name', '.product_name a::text')
            loader.add_css('price', '#content .price::text')
            loader.add_css('link', '.product_name a::attr(href)')
            drink_item = loader.load_item()

            drink_page = drink.css('.product_name a')
            yield from response.follow_all(drink_page, callback=self.parse_drink, meta={'drink_item': drink_item})
    
    def parse_drink(self, response):
        drink_item = response.meta['drink_item']
        loader = ItemLoader(item=drink_item, response=response)
        loader.add_css('summary', '.product-text-content p::text')
        loader.add_css('drink_volume', 'dd b::text')
        loader.add_css('alcohol_percentage', 'dt:nth-child(2) b::text')
        loader.add_css('origin_place', 'dd:nth-child(5) span::text')
        yield loader.load_item()