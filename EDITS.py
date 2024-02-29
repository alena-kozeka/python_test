import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

s = Service("C:\\Users\\appli\\PycharmProjects\\python_selenium\\geckodriver")
driver = webdriver.Firefox()
base_url = "https://www.lambdatest.com/selenium-playground/iframe-demo/"
driver.get(base_url)
driver.maximize_window()

iframe = driver.find_element(By.XPATH,"//iframe[@id='iFrame1']")
driver.switch_to.frame(iframe)

pole = driver.find_element(By.XPATH,"//div[@id='__next']/div/div[2]")
value_pole = pole.text
print(value_pole)

pole.send_keys(Keys.CONTROL + 'a')

click_edition_panel_bolt = driver.find_element(By.XPATH,"//button[@title='Bold']")
click_edition_panel_bolt.click()
print(click_edition_panel_bolt)


new_pole = driver.find_element(By.XPATH,"//div[@id='__next']/div/div[2]/b")
value_new_pole = new_pole.text
print(value_new_pole)

assert value_pole == value_new_pole
print('Редактирование успешно!')


