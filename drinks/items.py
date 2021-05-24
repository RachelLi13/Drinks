from re import M
from scrapy.item import Item, Field
from datetime import datetime 
from scrapy.loader.processors import MapCompose, TakeFirst

def remove_newline_tab(text):
    text = text.strip()
    return text

def remove_quotes(text):
    # strip the unicode quotes
    text = text.strip(u'\u201c'u'\u201d')
    return text

def remove_chars(text):
    text = text.replace(u'\xa0', u' ')
    return text


class DrinksItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    drink_name = Field(
        output_processor=TakeFirst()
    )
    drink_price = Field(
        input_processor=MapCompose(remove_newline_tab),
        output_processor=TakeFirst()
    )
    drink_link = Field(
        output_processor=TakeFirst()
    )
    drink_type = Field(
        output_processor=TakeFirst()
    )
    summary = Field(
        # input_processor=MapCompose(remove_quotes)
        output_processor=TakeFirst()
    )
    drink_volume = Field(
        input_processor=MapCompose(remove_chars),
        output_processor=TakeFirst()
    )
    alcohol_percentage = Field(
        output_processor=TakeFirst()
    )
    origin_place = Field(
        input_processor=MapCompose(remove_newline_tab),
        output_processor=TakeFirst()
    )

