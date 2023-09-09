from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service())
driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.ID,"Email").clear()
driver.find_element(By.ID,"Email").send_keys("admin@yourstore.com")

driver.find_element(By.ID,"Password").clear()
driver.find_element(By.ID,"Password").send_keys("admin")

driver.find_element(By.XPATH,"//button[@class='button-1 login-button']").click()

# for customers page
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


driver.find_element(By.XPATH,click_on_customers_xpath).click()
time.sleep(2)
driver.find_element(By.XPATH,customers_dropdown_Xpath).click()
time.sleep(5)
driver.find_element(By.XPATH,add_new_button_Xpath).click()
driver.find_element(By.ID,add_customer_email_id).send_keys("xyz@gmail.com")
# time.sleep(3)
driver.find_element(By.ID,add_customer_password_id).send_keys("admin")
# time.sleep(3)
driver.find_element(By.ID,add_customer_fist_name_id).send_keys("Milan")
# time.sleep(3)
driver.find_element(By.ID,add_customer_last_name_id).send_keys("Singh")
# time.sleep(3)
driver.find_element(By.ID,add_customer_gender_male_id).click()
# time.sleep(3)
driver.find_element(By.ID,add_customer_dob_id).send_keys("9/3/1993")
time.sleep(3)
driver.find_element(By.ID,add_customer_Company_id).send_keys("Giit")
time.sleep(3)
driver.find_element(By.ID,add_customer_istaxemp_Id).click()

# time.sleep(3)
# driver.find_element(By.XPATH,add_customer_NewsLetter_Xpath).send_keys('new india')
time.sleep(3)
driver.find_element(By.XPATH,add_customer_manager_of_vendor_Xpath).click()
time.sleep(2)
driver.find_element(By.XPATH,add_customer_chose_vendor1_xpath).click()
time.sleep(3)
driver.find_element(By.ID,add_customer_admin_comment_id).send_keys("amdin passed the comment")
time.sleep(4)
driver.find_element(By.XPATH,add_customer_save_xpath).click()
time.sleep(10)
driver.close()











driver.close()