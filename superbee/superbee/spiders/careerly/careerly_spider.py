from time import sleep

import scrapy

from superbee.superbee.config import constants
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


    def get_data(self):
        posts = self.driver.find_elements("xpath", "/html/body/div[1]/div[2]/div[2]/div/div[1]/div[2]/div/div")

        for post in posts:
            more_button = post.find_element("css selector", ".tw-text-slate-400.tw-cursor-pointer")
            more_button.click()