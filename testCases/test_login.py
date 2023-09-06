from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
from pageObjects.LoginPage import Login
from selenium.webdriver.chrome.service import Service
from utilities.readProperties import ReadConfig
import time
from utilities.logUtility import LogGeneration

class Test_001_login:
    base_url = ReadConfig.get_base_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGeneration.loggen()
    def test_homepagetitle(self,setup):
        self.logger.info("Test_001_login")
        self.driver = setup
        self.driver.get(self.base_url)
        title = self.driver.title
        self.logger.info("Title accessed")
        if title=='Your store. Login':
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot("Screenshots/test_homepagetitle.png")
            self.driver.close()
            assert False

    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.login_page = Login(self.driver)
        self.login_page.set_user_name(self.username)
        self.login_page.set_password(self.password)
        self.login_page.click_login()
        login_text = self.driver.title
        if login_text=="Dashboard / nopCommerce administration":
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot("Screenshots/test_login.png")
            self.driver.close()
            assert False

    def test_logout_function(self,setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.login_page = Login(self.driver)
        self.login_page.set_user_name(self.username)
        self.login_page.set_password(self.password)
        self.login_page.click_login()
        self.login_page.click_logout()
        Login_page_title = self.driver.title
        if Login_page_title=="Your store. Login":
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot("Screenshots/test_logout_function.png")
            self.driver.close()
            assert False



