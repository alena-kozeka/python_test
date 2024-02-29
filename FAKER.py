import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from faker import Faker

s = Service("C:\\Users\\appli\\PycharmProjects\\python_selenium\\geckodriver")
driver = webdriver.Firefox()
base_url = "https://www.saucedemo.com"
driver.get(base_url)
driver.maximize_window()



faker = Faker('en_US')

name = faker.first_name() + str(faker.random_int())
passw = faker.password()
print(name)
print(passw)

user_name = driver.find_element(By.XPATH,"//input[@id='user-name']") # ID
user_name.send_keys(name)
print("Input login")

password = driver.find_element(By.XPATH,"//input[@id='password']") # ID
password.send_keys(passw)
print("Input Password")