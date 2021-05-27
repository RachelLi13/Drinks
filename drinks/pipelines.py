from sqlalchemy.orm import sessionmaker
from scrapy.exceptions import DropItem
from drinks.models import Drink, db_connect, create_table
import logging


class SaveDrinksPipeline:
    def __init__(self):
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)

    
    def process_item(self, item, spider):
        #Save quotes in the database
        session = self.Session()
        drink = Drink()
        drink.name = item['drink_name']
        drink.price = item['drink_price']
        drink.link = item['drink_link']
        drink.type = item['drink_type']

        drink.origin_place = item['origin_place']
        drink.percentage= item['alcohol_percentage']
        drink.volume = item['drink_volume']
        drink.summary = item['summary']


        try:
            session.add(drink)
            session.commit()
        except:
            session.rollback()
            raise

        finally: 
            session.close()

        return item
