import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class AddCustomer:
    def __init__(self,driver):
        self.driver = driver
    
    click_on_customers_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    customers_dropdown_Xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    add_new_button_Xpath = "//a[@class='btn btn-primary']"
    add_customer_email_id = "Email"
    add_customer_password_id = "Password"
    add_customer_fist_name_id="FirstName"
    add_customer_last_name_id="LastName"
    add_customer_gender_male_id = "Gender_Male"
    add_customer_gender_female_id = "Gender_female"
    add_customer_dob_id = "DateOfBirth"
    add_customer_Company_id = "Company"
    add_customer_istaxemp_Id = "IsTaxExempt"
    add_customer_NewsLetter_Xpath = "//div[@class='input-group-append']//div[@role='listbox']"
    add_customer_manager_of_vendor_Xpath = "//select[@id='VendorId']"
    add_customer_managerofvendor_xpath="//select[@name='VendorId']"
    add_customer_chose_vendor1_xpath = "//option[text() = 'Vendor 1']"
    add_customer_chose_vendor2_xpath = "//option[text() = 'Vendor 2']"
    add_customer_admin_comment_id="AdminComment"
    add_customer_save_xpath = "//button[@name='save']"

    def open_customer_page(self):
        self.driver.find_element(By.XPATH,self.click_on_customers_xpath).click()
        self.driver.find_element(By.XPATH,self.customers_dropdown_Xpath).click()

    def add_new_customer(self):
        self.driver.find_element(By.XPATH,self.add_new_button_Xpath).click()

    def add_customer_email(self):
        self.driver.find_element(By.ID,self.add_customer_email_id).send_keys('milansingh163@gmail.com')

    def add_customer_password(self):
        self.driver.find_element(By.ID,self.add_customer_password_id).send_keys('AAaa@@33')

    def add_customer_FistName(self):
        self.driver.find_element(By.ID,self.add_customer_fist_name_id).send_keys('Milan')

    def add_customer_LastName(self):
        self.driver.find_element(By.ID,self.add_customer_last_name_id).send_keys('Singh')

    def gender_male(self):
        self.driver.find_element(By.ID,self.add_customer_gender_male_id).click()

    def gender_female(self):
        self.driver.find_element(By.ID,self.add_customer_gender_female_id).click()

    def add_dob(self):
        self.driver.find_element(By.ID,self.add_customer_dob_id).send_keys("9/3/1993")

    def company_name(self):
        self.driver.find_element(By.ID,self.add_customer_Company_id).send_keys("Giit solutions")

    def click_on_tax_exempt(self):
        self.driver.find_element(By.ID,self.add_customer_istaxemp_Id).click()

    def newsletter(self):
        self.driver.find_element(By.XPATH,self.add_customer_NewsLetter_Xpath).click()

    def add_manager_of_vendor(self):
        self.driver.find_element(By.XPATH,self.add_customer_manager_of_vendor_Xpath).click()
        self.driver.find_element(By.XPATH,self.add_customer_chose_vendor1_xpath).click()

    def add_admin_comment(self):
        self.driver.find_element(By.XPATH,self.add_customer_admin_comment_id).send_keys("let test admin comment")

    def save_button(self):
        self.driver.find_element(By.XPATH,self.add_customer_save_xpath).click()

