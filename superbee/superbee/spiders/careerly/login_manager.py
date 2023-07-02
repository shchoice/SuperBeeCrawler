import os
from time import sleep

from dotenv import load_dotenv
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from superbee.superbee.config import constants


class LoginManager:
    def __init__(self):
        options = Options()
        options.headless = False
        self.driver = webdriver.Firefox(options=options)
        load_dotenv(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), '.env.development'))

    def login(self):
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
