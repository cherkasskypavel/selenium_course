from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def text_to_func(*args, txt='', delimiter=''):
    from math import sin, log
    func_txt = list(filter(lambda x: 'x' in x, txt.split()))[0]
    func_txt = func_txt.strip(delimiter).replace('ln', 'log')
    vars_list = ['x', 'y', 'z']
    args = list(map(lambda x: int(x), args))
    for i in range(len(args)):
        func_txt = func_txt.replace(vars_list[i], f'int(args[{i}])')
    print(func_txt)
    result = eval(func_txt)
    return result

with webdriver.Chrome() as browser:
    link = 'http://suninjuly.github.io/explicit_wait2.html'
    browser.get(link)
    browser.implicitly_wait(1)

    cost = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    book_button = browser.find_element(By.ID, 'book')
    book_button.click()

    browser.execute_script('window.scrollBy(0, 400);')
    time.sleep(1)
    func_text = browser.find_element(By.CSS_SELECTOR, 'form label .nowrap:nth-child(1)').text

    val = browser.find_element(By.ID, 'input_value').text

    result = text_to_func(val, txt=func_text, delimiter=',')

    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(result)

    button = browser.find_element(By.ID, 'solve')
    button.click()
    time.sleep(4)
