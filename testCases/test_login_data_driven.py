from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
from pageObjects.LoginPage import Login
from selenium.webdriver.chrome.service import Service
from utilities.readProperties import ReadConfig
import time
from utilities.logUtility import LogGeneration
from utilities import read_excel_data_util
import time


class Test_001_login:
    base_url = ReadConfig.get_base_url()
    login_data_path = ".\\TestData\\logindata.xlsx"
    # username = ReadConfig.get_username()
    # password = ReadConfig.get_password()
    log_message = LogGeneration.loggen()

    # writing test case method for data driven excel file 
    def test_login_data_driven(self,setup):
        self.log_message.info("********* data driven test started **************")
        self.driver = setup
        self.driver.get(self.base_url)
        self.login_page = Login(self.driver)

        self.row = read_excel_data_util.getRowCount(self.login_data_path,'Sheet1')
        self.col = read_excel_data_util.getColumnCount(self.login_data_path,'Sheet1')
        self.result = []
        self.expected_login_text="Dashboard / nopCommerce administration"

        for r in range(2,self.row+1):
            self.user = read_excel_data_util.readData(self.login_data_path,'Sheet1',r,1)
            self.password = read_excel_data_util.readData(self.login_data_path,'Sheet1',r,2)
            self.exp = read_excel_data_util.readData(self.login_data_path,'Sheet1',r,3)
            self.login_page.set_user_name(self.user)
            self.login_page.set_password(self.password)
            self.login_page.click_login()
            self.log_message.info("********* logged in **************")

            time.sleep(2)
            self.actula_login_text = self.driver.title
            self.log_message.info("logged out")

            time.sleep(5)
            

            if self.actula_login_text== self.expected_login_text:
                if self.exp=="Pass":
                    self.result.append("Pass")
                    self.login_page.click_logout()
                    time.sleep(2)
                elif self.exp=="Fail":
                    self.result.append('Fail')
            elif self.actula_login_text!=self.expected_login_text:
                if self.exp=='Fail':
                    self.result.append('Pass')
                elif self.exp=="Pass":
                    self.result.append("Fail")
            self.log_message.info("result for the test  {}".format(self.result))

        if "Fail" in self.result:
            assert False
            self.log_message.info("********* data driven test failed**************")
        else:
            assert True
            self.log_message.info("********* data driven passed failed**************")





                




