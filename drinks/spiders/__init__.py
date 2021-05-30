from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from drinks.spiders.coolers import CoolerSpider
from drinks.spiders.spirits import SpiritsSpider
from drinks.spiders.beers_ciders import Beer_CiderSpider
from drinks.spiders.wines import WinesSpider

process = CrawlerProcess(get_project_settings())
process.crawl(CoolerSpider)
process.crawl(SpiritsSpider)
process.crawl(Beer_CiderSpider)
process.crawl(WinesSpider)
process.start()