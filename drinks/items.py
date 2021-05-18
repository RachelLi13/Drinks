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
    name = Field()
    price = Field(
        input_processor=MapCompose(remove_chars)
    )
    link = Field()
    summary = Field()
    drink_volume = Field()
    alcohol_percentage = Field()
    origin_place = Field(
        input_processor=MapCompose(remove_chars)
    )

