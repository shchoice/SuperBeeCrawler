from time import sleep

import scrapy
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


class CareerlySpider(scrapy.Spider):
    name = "spider01"
    start_urls = ['https://careerly.co.kr/']

    def __init__(self):
        options = Options()
        options.headless = False
        self.driver = webdriver.Firefox(options=options)

    def start_requests(self):
        login_url = "https://careerly.co.kr/login"
        login_data = {
            "email": "",
            "password": ""
        }

        self.driver.get(login_url)

        self.driver.find_element("id", "email").send_keys(login_data["email"])
        self.driver.find_element("id", "password").send_keys(login_data["password"])

        self.driver.find_element("css selector", "button.btn.btn-lg.btn-block.btn-coral-600.tw-mb-3").click()

        sleep(10)

        self.get_data()

    def get_data(self):
        posts = self.driver.find_elements("xpath", "/html/body/div[1]/div[2]/div[2]/div/div[1]/div[2]/div/div")

        for post in posts:
            more_button = post.find_element("css selector", ".tw-text-slate-400.tw-cursor-pointer")
            more_button.click()