import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

s = Service(executable_path='/Users/atabekov/PycharmProjects/pythonProject/chromedriver-mac-x64/chromedriver')
driver = webdriver.Chrome(service=s)

try:
    driver.maximize_window()
    driver.get('https://kolesa.kz/')

    common_cars = driver.find_element(By.XPATH, "//span[contains(@title, 'Легковые')]").click()
    year_from = driver.find_element(By.ID, 'year[from]')
    year_from.clear()
    year_from.send_keys('2005')

    year_to = driver.find_element(By.ID, 'year[to]')
    year_to.clear()
    year_to.send_keys('2010')

    price_from = driver.find_element(By.ID, 'price[from]')
    price_from.clear()
    price_from.send_keys('200000')

    price_to = driver.find_element(By.ID, 'price[to]')
    price_to.clear()
    price_to.send_keys('5000000')
    show_results = driver.find_element(By.XPATH, "//span[contains(text(), 'Показать')]").click()

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()