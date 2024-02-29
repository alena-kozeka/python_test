from datetime import datetime, timedelta
import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


# s = Service("C:\\Users\\appli\\PycharmProjects\\python_selenium\\geckodriver")
# driver = webdriver.Firefox()
# base_url = "https://demoqa.com/date-picker"
# driver.get(base_url)
# driver.maximize_window()

# # checkbox = driver.find_element(By.XPATH,"//button[@aria-label='Toggle']")
# # checkbox.click()
#
# action = ActionChains(driver)
# # double = driver.find_element(By.XPATH,"//button[@id='doubleClickBtn']")
# # action.double_click(double).perform()
#
# right_click = driver.find_element(By.XPATH, "//button[@id='rightClickBtn']")
# action.context_click(right_click).perform()

# new_date = driver.find_element(By.XPATH, "//input[@id='datePickerMonthYearInput']")
# new_date.clear()
# time.sleep(5)
# new_date.send_keys("01/10/2024")
# time.sleep(5)
# new_date.send_keys(Keys.RETURN)


"""Получаем текущую дату и время"""
current_date = datetime.now()
print(current_date)

"""Убавляем 10 дней от текущей даты"""
new_date = current_date - timedelta(days=10)
print(new_date)

"""Добавляем 10 дней к текущей даты"""
old_date = current_date + timedelta(days=10)
print(old_date)
