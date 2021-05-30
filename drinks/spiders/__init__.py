from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from drinks.spiders.coolers import CoolerSpider
from drinks.spiders.spirits import SpiritsSpider
from drinks.spiders.beers_ciders import Beer_CiderSpider

process = CrawlerProcess(get_project_settings())
process.crawl(CoolerSpider)
process.crawl(SpiritsSpider)
process.crawl(Beer_CiderSpider)
process.start()