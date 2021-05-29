from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from drinks.spiders.coolers import CoolerSpider
from drinks.spiders.spirits import SpiritsSpider

process = CrawlerProcess(get_project_settings())
process.crawl(CoolerSpider)
# process.crawl(SpiritsSpider)
process.start()