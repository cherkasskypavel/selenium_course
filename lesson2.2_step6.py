from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from my_funcs import str_to_func

# def text_to_func(x, text=str()):
#     from math import sin, log
#     x = int(x)
#     return eval(text.strip(',').replace('ln', 'log'))

def text_to_func(*args, txt='', delimiter=''):
    from math import sin, log
    func_txt = list(filter(lambda x: 'x' in x, txt.split()))[0]
    func_txt = func_txt.strip(delimiter).replace('ln', 'log')
    vars_list = ['x', 'y', 'z']
    args = list(map(lambda x: int(x), args))
    for i in range(len(args)):
        func_txt = func_txt.replace(vars_list[i], f'int(args[{i}])')
    result = eval(func_txt)
    return result

with webdriver.Chrome() as browser:
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    func_text = browser.find_element(By.CSS_SELECTOR, 'div.form-group label span:nth-child(1)').text

    x = browser.find_element(By.ID, 'input_value').text

    result = text_to_func(x, txt=func_text, delimiter=',')
    # result = text_to_func(x, func_text)

    input_field = browser.find_element(By.ID, 'answer')
    input_field.send_keys(result)

    robot_checkbox = browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]')
    robot_checkbox.click()
    time.sleep(1)

    browser.execute_script("window.scrollBy(0, 100);")

    robot_radio = browser.find_element(By.ID, 'robotsRule')
    robot_radio.click()

    submit_button = browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
    submit_button.click()
    time.sleep(4)