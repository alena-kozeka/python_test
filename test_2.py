

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


s = Service("C:\\Users\\appli\\PycharmProjects\\python_selenium\\geckodriver")
driver = webdriver.Firefox()
base_url = "https://www.saucedemo.com"
driver.get(base_url)
driver.maximize_window()

login_standard_user = "standard_use"
password_all = "secret_sauc"

user_name = driver.find_element(By.XPATH,"//input[@id='user-name']") # ID
user_name.send_keys(login_standard_user)
print("Input login")

password = driver.find_element(By.XPATH,"//input[@id='password']") # ID
password.send_keys(password_all)
print("Input Password")

button_login = driver.find_element(By.ID,"login-button")
button_login.click()
print("Click Login Button")

warning_text = driver.find_element(By.XPATH,"//h3[@data-test='error']")
value_warning_text = warning_text.text
assert  value_warning_text == "Epic sadface: Username and password do not match any user in this service"
print("Good Test")

driver.refresh()

