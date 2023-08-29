from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

with webdriver.Chrome() as browser:
    link = 'http://suninjuly.github.io/file_input.html'
    browser.get(link)

    restrict_list = browser.find_elements(By.CSS_SELECTOR, 'input[type="text"]:required')

    for i in restrict_list:
        i.send_keys('pass')


    load_file = browser.find_element(By.ID, 'file')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'text.txt')
    print(file_path)
    load_file.send_keys(file_path)

    submit = browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
    submit.click()
    time.sleep(4)

