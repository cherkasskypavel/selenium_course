import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

with webdriver.Chrome() as browser:
    browser.get('https://suninjuly.github.io/math.html')

    x_var = browser.find_element(By.ID, 'input_value').text
    result = calc(x_var)

    answer_input = browser.find_element(By.ID, 'answer')
    answer_input.send_keys(result)
    time.sleep(3)

    chckbx = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox:required')
    chckbx.click()
    time.sleep(3)

    radio = browser.find_element(By.CSS_SELECTOR, '.form-radio-custom [for="robotsRule"]')
    radio.click()
    time.sleep(3)

    submit = browser.find_element(By.CSS_SELECTOR, '.btn.btn-default')
    submit.click()
    time.sleep(4)