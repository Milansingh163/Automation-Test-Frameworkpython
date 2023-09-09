from selenium.webdriver.common.by import By
from selenium import webdriver

class Login:
    def __init__(self,driver):
        self.driver = driver
    
    textbox_usesrname_id  = "Email"
    textbox_password_id  =  "Password"
    button_login_xpath = "//button[normalize-space()='Log in']"
    link_logout_lintext = "Logout"

    def set_user_name(self,username):
        self.driver.find_element(By.ID,self.textbox_usesrname_id).clear()
        self.driver.find_element(By.ID,self.textbox_usesrname_id).send_keys(username)


    def set_password(self,password):
        self.driver.find_element(By.ID,self.textbox_password_id).clear()
        self.driver.find_element(By.ID,self.textbox_password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()

    def click_logout(self):
        self.driver.find_element(By.LINK_TEXT,self.link_logout_lintext).click()


    

