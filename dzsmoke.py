from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

s = Service("C:\\Users\\appli\\PycharmProjects\\python_selenium\\geckodriver")
driver = webdriver.Firefox()
base_url = "https://www.saucedemo.com"
driver.get(base_url)
driver.maximize_window()

login_user_name = "standard_user"
password_all = "secret_sauce"

username = driver.find_element(By.XPATH, "//input[@id='user-name']")
username.send_keys(login_user_name)
print("Input login")

password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(password_all)
print("Input Password")

button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
button_login.click()
print("Click Button Login")

"""INFO PRODUCT #1"""
product_1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
value_product_1 = product_1.text
print(value_product_1)

price_product_1 = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div")
value_price_product_1 = price_product_1.text
print(value_price_product_1)

select_product_1 = driver.find_element(By.XPATH,"//button[@id='add-to-cart-sauce-labs-backpack']")
select_product_1.click()
print("Select Product 1")

"""INFO PRODUCT #2"""
product_2 = driver.find_element(By.XPATH, "//a[@id='item_0_title_link']")
value_product_2 = product_2.text
print(value_product_2)

price_product_2 = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[2]/div[2]/div[2]/div")
value_price_product_2 = price_product_2.text
print(value_price_product_2)

Select_product_2 = driver.find_element(By.XPATH, "//button[@id = 'add-to-cart-sauce-labs-bike-light']")
Select_product_2.click()
print("Select Product 2")

"""CART"""
cart = driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']/a")
cart.click()
print("Enter Cart")

"""Info cart product 1"""
cart_product_1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
value_cart_product_1 = cart_product_1.text
print(value_cart_product_1)
assert value_product_1 == value_cart_product_1
print("INFO CART PRODUCT GOOD 1")

price_cart_product_1 = driver.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div")
value_price_cart_product_1 = price_cart_product_1.text
print(value_price_cart_product_1)
assert value_price_product_1== value_price_cart_product_1
print("INFO CART PRICE PRODUCT GOOD 1")

cart_product_2 = driver.find_element(By.XPATH, "//a[@id='item_0_title_link']")
value_cart_product_2 = cart_product_2.text
print(value_cart_product_2)
assert value_product_2 == value_cart_product_2
print("INFO CART PRODUCT GOOD 1")

price_cart_product_2 = driver.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[4]/div[2]/div[2]/div")
value_cart_product_2 = price_cart_product_2.text
print(value_cart_product_2)
assert value_price_product_2 == value_cart_product_2
print("INFO CART PRICE PRODUCT GOOD 2")

checkout = driver.find_element(By.XPATH, "//button[@id='checkout']")
checkout.click()
print("CLICK CHEKOUT")

"""USER INFORMATION"""
first_name = driver.find_element(By.XPATH, "//input[@id='first-name']")
first_name.send_keys("Ivan")
print("Input First name")

last_name = driver.find_element(By.XPATH, "//input[@id='last-name']")
last_name.send_keys("Ivanov")

zip = driver.find_element(By.XPATH, "//input[@id='postal-code']")
zip.send_keys("123456")
print("Input Zip")

continue_button = driver.find_element(By.XPATH, "//input[@id='continue']")
continue_button.click()
print("CLICK CONTINUE")

"""Info Finish product 1"""
finish_product_1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
value_finish_product_1 = finish_product_1.text
print(value_finish_product_1)
assert value_product_1 == value_finish_product_1
print("Info Finish product 1 GOOD")

price_finish_product_1 = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div")
value_price_finish_product_1 = price_finish_product_1.text
print(value_price_finish_product_1)
assert value_price_product_1 == value_price_finish_product_1
print("Info Finish  price product 1 GOOD")

"""Info Finish product 2"""
finish_product_2 = driver.find_element(By.XPATH, "//a[@id='item_0_title_link']")
value_finish_product_2 = finish_product_2.text
print(value_finish_product_2)
assert value_product_2 == value_finish_product_2
print("Info Finish product 2 GOOD")

price_finish_product_2 = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[4]/div[2]/div[2]/div")
value_price_finish_product_2 = price_finish_product_2.text
print(value_price_finish_product_2)
assert (value_price_product_2 == value_price_finish_product_2)
print("Info Finish  price product 2 GOOD")

value_price_finish_product_1 = price_finish_product_1.text
res_value_price_finish_product_1 = float(value_price_finish_product_1.replace('$', ''))
print(res_value_price_finish_product_1)

value_price_finish_product_2 = price_finish_product_2.text
res_value_price_finish_product_2 = float(value_price_finish_product_2.replace('$', ''))
print(res_value_price_finish_product_2)

summary_products = res_value_price_finish_product_1 + res_value_price_finish_product_2
print(summary_products)


price_total = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[6]")
value_price_total = price_total.text
res_value_price_total = float(value_price_total.replace('Item total: $', ''))
print(res_value_price_total)
assert summary_products == res_value_price_total
print("ITEM TOTAL GOOOOOOOOOD")






































