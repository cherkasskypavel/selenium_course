from selenium import webdriver
import pytest


@pytest.fixture(scope='function')
def browser():
    print('\nОткрываем браузер')
    browser = webdriver.Chrome
    yield print('\nЗакрываем браузер')
    browser.close()

