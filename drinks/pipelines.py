from sqlalchemy.orm import sessionmaker
from scrapy.exceptions import DropItem


class DrinksPipeline:
    def process_item(self, item, spider):
        return item
