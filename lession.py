import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

s = Service("C:\\Users\\appli\\PycharmProjects\\python_selenium\\chromedriver2")
driver = webdriver.Chrome()

# s = Service("C:\\Users\\appli\\PycharmProjects\\python_selenium\\geckodriver")
# driver = webdriver.Firefox()

driver.get("https://www.saucedemo.com")
driver.maximize_window()

# user_name = driver.find_element(By.ID,"user-name") # ID
# user_name = driver.find_element(By.NAME,"user-name")# NAME
user_name = driver.find_element(By.XPATH,"//input[@id='user-name']") # ID XPATH
# user_name = driver.find_element(By.XPATH,'//*[@id="user-name"]') # FULL XPATH
user_name.send_keys("standard_user")

user_pass = driver.find_element(By.CSS_SELECTOR, '#password') #CSS SELECTOR
user_pass.send_keys("secret_sauce")

button_login = driver.find_element(By.ID,"login-button")
button_login.click()

# time.sleep(10)
# driver.close()
