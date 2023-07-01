import sys
print(sys.path)

from scrapy.crawler import CrawlerProcess

from spiders.careerly_spider import CareerlySpider

if __name__ == "__main__":
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })

    process.crawl(CareerlySpider)
    process.start()