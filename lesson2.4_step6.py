from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    link = 'http://suninjuly.github.io/cats.html'
    browser.get(link)

    button = browser.find_element(By.ID, 'button')