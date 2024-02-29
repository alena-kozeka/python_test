import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


s = Service("C:\\Users\\appli\\PycharmProjects\\python_selenium\\chromedriver2")
driver = webdriver.Chrome()
base_url = "https://www.saucedemo.com"
driver.get(base_url)
driver.maximize_window()

login_standard_user = "standard_user"
password_all = "secret_sauce"

user_name = driver.find_element(By.XPATH,"//input[@id='user-name']") # ID
user_name.send_keys(login_standard_user)
print("Input login")

password = driver.find_element(By.XPATH,"//input[@id='password']") # ID
password.send_keys(password_all)
print("Input Password")
password.send_keys(Keys.RETURN)

filter = driver.find_element(By.XPATH,"//select[@data-test='product_sort_container']")
filter.click()
print("click filter")
time.sleep(5)
filter.send_keys(Keys.DOWN)
print("click down")
time.sleep(5)
filter.send_keys(Keys.DOWN)
print("click down 2 ")
time.sleep(5)
filter.send_keys(Keys.RETURN)
print("return")





# password = driver.find_element(By.XPATH,"//input[@id='password']") # ID
# password.send_keys(password_all)
# print("Input Password")
#
# button_login = driver.find_element(By.ID,"login-button")
# button_login.click()
# print("Click Login Button")
#
# text_products = driver.find_element(By.XPATH, "//span[@class='title']")
# value_text_products = text_products.text
# print(value_text_products)
# assert value_text_products == "Products"
# print("Good")
#
# url = "https://www.saucedemo.com/inventory.html"
# get_url = driver.current_url
# print(get_url)
# assert url == get_url
# print("Good url")
#
# driver.refresh()