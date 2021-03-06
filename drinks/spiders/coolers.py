import scrapy
from scrapy.loader import ItemLoader
from drinks.items import DrinksItem

class CoolerSpider(scrapy.Spider):
    name='coolers'

    start_urls = ['https://www.lcbo.com/webapp/wcs/stores/servlet/en/lcbo/coolers-18-1/coolers-18029',
    'https://www.lcbo.com/webapp/wcs/stores/servlet/en/lcbo/coolers-18-1/premixed-cocktails-18030']

    def parse(self, response):
        drinks = response.css('.product')
        for drink in drinks:
            loader = ItemLoader(item = DrinksItem(), selector = drink)
            loader.add_css('drink_name', '.product_name a::text')
            loader.add_css('drink_price',  '.price::text')
            loader.add_css('drink_link', '.product_name a::attr(href)')
            drink_item = loader.load_item()


            drink_page = drink.css('.product_name a')
            yield from response.follow_all(drink_page, callback=self.parse_drink, meta={'drink_item': drink_item})
    
        pagination_link = response.css('#WC_SearchBasedNavigationResults_pagination_link_right_categoryResults::attr(href)').get()      
        if drinks:
            yield response.follow(pagination_link, callback=self.parse)

    
    def parse_drink(self, response):
        drink_item = response.meta['drink_item']
        loader = ItemLoader(item=drink_item, response=response)
        loader.add_css('summary', '.product-text-content p::text')
        loader.add_css('drink_volume', 'dd b::text')
        loader.add_css('alcohol_percentage', 'dd:nth-child(3) span::text')
        loader.add_css('origin_place', 'dd:nth-child(5) span::text')
        loader.add_css('drink_type', '#widget_breadcrumb li+ li a::text')
        yield loader.load_item()
