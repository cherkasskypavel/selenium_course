from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture(scope="session")
def browser():
    print('\nОткрываем браузер')
    browser = webdriver.Chrome()
    browser.implicitly_wait(1)
    yield browser
    print('\nЗакрываем браузер')
    browser.close()

