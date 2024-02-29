import datetime

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


s = Service("C:\\Users\\appli\\PycharmProjects\\python_selenium\\geckodriver")
driver = webdriver.Firefox()
base_url = "https://html5css.ru/howto/howto_js_rangeslider.php"
driver.get(base_url)
driver.maximize_window()

action = ActionChains(driver)


square = driver.find_element(By.XPATH,"//input[@id='id2']") # ID
action.click_and_hold(square).move_by_offset(20,0).release().perform()
print("square +")


