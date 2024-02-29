import datetime
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


s = Service("C:\\Users\\appli\\PycharmProjects\\python_selenium\\geckodriver")
driver = webdriver.Firefox()
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

button_login = driver.find_element(By.ID,"login-button")
button_login.click()
print("Click Login Button")

"""info product #1"""
product_1 = driver.find_element(By.XPATH,"//a[@id='item_4_title_link']")
value_product_1 = product_1.text
print(value_product_1)

price_product_1 = driver.find_element(By.XPATH,"//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div")
value_price_product_1 = price_product_1.text
print(value_price_product_1)

select_product_1 = driver.find_element(By.XPATH,"//button[@id='add-to-cart-sauce-labs-backpack']")
select_product_1.click()
print("Select Product 1")


cart = driver.find_element(By.XPATH,"//a[@class='shopping_cart_link']")
cart.click()
print("Enter Cart")

"""Info cart product 1"""
cart_product_1 = driver.find_element(By.XPATH,"//a[@id='item_4_title_link']")
value_cart_product_1 = cart_product_1.text
print(value_cart_product_1)
assert value_product_1 == value_cart_product_1
print("INFO cart product 1 GOOD")

cart_price_product_1 = driver.find_element(By.XPATH,"//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div")
value_cart_price_product_1 = cart_price_product_1.text
print(value_cart_price_product_1)
assert value_price_product_1 == value_cart_price_product_1
print("INFO price_product_1 GOOD")

checkout = driver.find_element(By.XPATH,"//button[@id='checkout']")
checkout.click()
print("Click Checkout")

"""Select User Info"""

first_name = driver.find_element(By.XPATH,"//input[@id='first-name']")
first_name.send_keys("Alex")
print("Select FIST NAME")

last_name = driver.find_element(By.XPATH,"//input[@id='last-name']")
last_name.send_keys("Ivanov")
print("Select LAST NAME")

zip = driver.find_element(By.XPATH,"//input[@id='postal-code']")
zip.send_keys("1234")
print("Select ZIP")

button_continue = driver.find_element(By.XPATH,"//input[@id='continue']")
button_continue.click()
print("Click Button Continue")

"""Info Finish product 1"""
finish_product_1 = driver.find_element(By.XPATH,"//a[@id='item_4_title_link']")
value_finish_product_1 = finish_product_1.text
print(value_finish_product_1)
assert value_product_1 == value_finish_product_1
print("INFO finish product 1 GOOD")

finish_price_product_1 = driver.find_element(By.XPATH,"//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div")
value_finish_price_product_1 = finish_price_product_1.text
print(value_finish_price_product_1)
assert value_price_product_1 == value_finish_price_product_1
print("INFO finish price product 1 GOOD")



summary_price = driver.find_element(By.XPATH,"//*[@id='checkout_summary_container']/div/div[2]/div[6]")
value_summary_price = summary_price.text
print(value_summary_price)

item_total = "Item total: " + value_finish_price_product_1
print(item_total)
assert value_summary_price == item_total
print("TOTAL SUMMARY PRICE GOOD")







