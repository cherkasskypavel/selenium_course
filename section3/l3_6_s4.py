from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

link = 'https://stepik.org/lesson/236895/step/1'

class TestStepik():

    def test_signin_check(self, browser):
        browser.get(link)
        signin_button = browser.find_element(By.ID, 'ember33')
        signin_button.click()

        # найти объект с классом .modal-dialog-inner,

