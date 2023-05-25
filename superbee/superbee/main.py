import sys
print(sys.path)

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from spiders.CareerlySpider import CareerlySpider

if __name__ == "__main__":
    project_settings = get_project_settings()
    project_settings.setmodule('superbee.settings')
    process = CrawlerProcess(project_settings)

    process.crawl(CareerlySpider)
    process.start()