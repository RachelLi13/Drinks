import scrapy 
from scrapy.loader import ItemLoader
from drinks.items import DrinksItem



class SpiritsSpider(scrapy.Spider):
    name="beers_ciders"
    # allowed_domains = ['https://lcbo.com']
    start_urls = ['https://www.lcbo.com/webapp/wcs/stores/servlet/en/lcbo/beer-cider-16/lager-16023',
    'https://www.lcbo.com/webapp/wcs/stores/servlet/en/lcbo/beer-cider-16/ale-16022',
    'https://www.lcbo.com/webapp/wcs/stores/servlet/en/lcbo/beer-cider-16/hybrid-16024',
    'https://www.lcbo.com/webapp/wcs/stores/servlet/en/lcbo/beer-cider-16/specialty-16025',
    'https://www.lcbo.com/webapp/wcs/stores/servlet/en/lcbo/beer-cider-16/cider-16028',
    'https://www.lcbo.com/webapp/wcs/stores/servlet/en/lcbo/beer-cider-16/radler-shandy-16117']


    def parse(self, response):
        # drink_number_total = response.css('.spaced-character::text').get()
        # drink_number_total = int(drink_number_total)
        # self.logger.info(drink_number_total)
        # drink_number = 0
        drinks = response.css('.product')
        for drink in drinks:
            # yield {
            #     'name': drink.css(".product_name a::text").get(),
            #     'price': drink.css("#content .price::text").get(),
            #     'link': drink.css(".product_name a::attr(href)").get()
            # }
            # drink_number += 1
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
        loader.add_css('drink_type', '#widget_breadcrumb li~ li+ li a::text')
        yield loader.load_item()
