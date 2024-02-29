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

menu = driver.find_element(By.XPATH,"//button[@id='react-burger-menu-btn']")
menu.click()
print("Click menu Button")
time.sleep(3)

link_about = driver.find_element(By.XPATH,"//a[@id='about_sidebar_link']")
link_about.click()
print("Click link_about")
time.sleep(5)
driver.back()
print("Go Back")
time.sleep(5)
driver.forward()
print("Go Forward")
time.sleep(5)
