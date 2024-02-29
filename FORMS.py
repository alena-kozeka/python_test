import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

s = Service("C:\\Users\\appli\\PycharmProjects\\python_selenium\\geckodriver")
driver = webdriver.Firefox()
base_url = "https://www.lambdatest.com/selenium-playground/simple-form-demo"
driver.get(base_url)
driver.maximize_window()

# message = 'Hello World'
# input_pole = driver.find_element(By.XPATH,"//input[@id='user-message']")
# input_pole.send_keys(message)
# print("Input pole")
#
# button_click = driver.find_element(By.XPATH,"//button[@id='showInput']")
# button_click.click()
# print("button_click")
#
# pole_message = driver.find_element(By.XPATH,"//p[@id='message']")
# value_pole_message = pole_message.text
# print(value_pole_message)
# assert value_pole_message == message
# print('Значения верны')

num1 = 121
num2 = 101

input_pole_1 = driver.find_element(By.XPATH,"//input[@id='sum1']")
input_pole_1.send_keys(num1)
print("Input pole 1")
time.sleep(3)
input_pole_2 = driver.find_element(By.XPATH,"//input[@id='sum2']")
input_pole_2.send_keys(num2)
print("Input pole 2")
time.sleep(3)
button_click = driver.find_element(By.XPATH,"//button[contains(text(),'Get Sum')]")
button_click.click()
print("button_click")
time.sleep(3)
result_pole = driver.find_element(By.XPATH,"//p[@id='addmessage']")
value_result_pole = result_pole.text
print("value_result_pole")
sum = num1 + num2
assert value_result_pole == str(sum)
print('Значения верны')
