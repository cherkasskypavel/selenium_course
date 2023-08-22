from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

with webdriver.Chrome() as browser:
    browser.get('https://suninjuly.github.io/selects1.html')

    num1 = int(browser.find_element(By.ID, 'num1').text)
    num2 = int(browser.find_element(By.ID, 'num2').text)

    select_button = Select(browser.find_element(By.ID, 'dropdown'))
    select_button.select_by_value(str(num1 + num2))

    submit = browser.find_element(By.CSS_SELECTOR, '.btn.btn-default')
    submit.click()
    time.sleep(4)
