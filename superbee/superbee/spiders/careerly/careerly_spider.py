from time import sleep

import scrapy

from superbee.superbee.config import constants
from superbee.superbee.spiders.careerly.data_extractor import get_data
from superbee.superbee.spiders.careerly.login_manager import LoginManager


class CareerlySpider(scrapy.Spider):
    name = constants.CAREERLY_SPIDER_NAME
    start_urls = [constants.CAREERLY_URL_HOME]

    def __init__(self):
        self.login_manager = LoginManager()

    def start_requests(self):
        self.login_manager.login()

        for i in range(10):
            print("scroll down")
            self.login_manager.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(2)

        get_data(self.login_manager.driver)
