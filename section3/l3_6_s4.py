from selenium.webdriver.common.by import By
import pytest

link = 'https://stepik.org/lesson/236895/step/1'

class TestStepik():

    def test_signup_check(self, browser):
        browser.get(link)

