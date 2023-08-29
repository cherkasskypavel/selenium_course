from selenium import webdriver
import pytest


@pytest.fixture(scope='function')
def browser():
    print('\nОткрываем браузер')
    browser = webdriver.Chrome
    browser.implicitly_wait(5)
    yield print('\nЗакрываем браузер')
    browser.close()

