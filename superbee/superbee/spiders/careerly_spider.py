import os
from time import sleep

import scrapy
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from superbee.superbee.config import constants


class CareerlySpider(scrapy.Spider):
    name = constants.CAREERLY_SPIDER_NAME
    start_urls = [constants.CAREERLY_URL_HOME]
    load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env.development'))

    def __init__(self):
        options = Options()
        options.headless = False
        self.driver = webdriver.Firefox(options=options)

    def start_requests(self):
        login_url = constants.CAREERLY_URL_LOGIN
        login_data = {
            "email": os.getenv("CAREERLY_USER_EMAIL"),
            "password": os.getenv("CAREERLY_USER_PASSWORD")
        }

        self.driver.get(login_url)

        self.driver.find_element("id", "email").send_keys(login_data["email"])
        self.driver.find_element("id", "password").send_keys(login_data["password"])

        self.driver.find_element("xpath", "/html/body/div[1]/div[2]/div[2]/div[1]/div/form/div[3]/button[1]").click()

        sleep(5)

        for i in range(10):
            print("scroll down")
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(2)


    def get_data(self):
        posts = self.driver.find_elements("xpath", "/html/body/div[1]/div[2]/div[2]/div/div[1]/div[2]/div/div")

        for post in posts:
            more_button = post.find_element("css selector", ".tw-text-slate-400.tw-cursor-pointer")
            more_button.click()