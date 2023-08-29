import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

with webdriver.Chrome() as browser:
    browser.get('https://suninjuly.github.io/get_attribute.html')

    x_image = browser.find_element(By.ID, 'treasure')
    x_var = x_image.get_attribute('valuex')



    answer_input = browser.find_element(By.ID, 'answer')
    answer_input.send_keys(calc(x_var))


    chckbx = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox:required')
    chckbx.click()

    radio = browser.find_element(By.ID, 'robotsRule')
    radio.click()
    time.sleep(3)

    submit = browser.find_element(By.CSS_SELECTOR, '.btn.btn-default')
    submit.click()
    time.sleep(6)