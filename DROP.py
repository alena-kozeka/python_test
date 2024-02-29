import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

s = Service("C:\\Users\\appli\\PycharmProjects\\python_selenium\\geckodriver")
driver = webdriver.Firefox()
# base_url = "https://www.saucedemo.com"
# driver.get(base_url)
# driver.maximize_window()

# login_standard_user = "standard_user"
# password_all = "secret_sauce"
#
# user_name = driver.find_element(By.XPATH,"//input[@id='user-name']") # ID
# user_name.send_keys(login_standard_user)
# print("Input login")
#
# password = driver.find_element(By.XPATH,"//input[@id='password']") # ID
# password.send_keys(password_all)
# print("Input Password")
#
# button_login = driver.find_element(By.ID,"login-button")
# button_login.click()
# print("Click Login Button")
#
# select = Select(driver.find_element(By.XPATH,"//select[@class='product_sort_container']"))
# time.sleep(5)
# """1 вариант"""
# select.select_by_visible_text('Name (Z to A)')
# """2 вариант"""
# # select.select_by_value('za')

"""DROP  на другом сайте"""

base_url = "https://www.lambdatest.com/selenium-playground/jquery-dropdown-search-demo"
driver.get(base_url)
driver.maximize_window()
time.sleep(3)
click_drop = driver.find_element(By.XPATH,"//span[@aria-labelledby='select2-country-container']")
click_drop.click()
print("Click drop")
time.sleep(3)
# click_country = driver.find_element(By.XPATH,"(//li[@class='select2-results__option'])[3]")
# click_country.click()
# print("Click country")

input_country = driver.find_element(By.XPATH,"(//input[@class='select2-search__field'])[2]")
input_country.send_keys('Bangladesh')
time.sleep(3)
input_country.send_keys(Keys.RETURN)














