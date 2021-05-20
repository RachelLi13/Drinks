from re import M
from scrapy.item import Item, Field
from datetime import datetime 
from scrapy.loader.processors import MapCompose, TakeFirst

def remove_chars(text):
    text = text.strip()
    return text
   


class DrinksItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    drink_name = Field()
    drink_price = Field(
        input_processor=MapCompose(remove_chars)
    )
    drink_link = Field()
    drink_type = Field()
    summary = Field()
    drink_volume = Field()
    alcohol_percentage = Field()
    origin_place = Field(
        input_processor=MapCompose(remove_chars)
    )

