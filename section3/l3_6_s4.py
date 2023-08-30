import dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from dotenv import load_dotenv
import os
import time
import math

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

# добавить переменные окружения
link1 = 'https://stepik.org/lesson/236895/step/1'
login = os.getenv('S_LOGIN')
password = os.getenv('S_PASSWORD')
link_list = ['https://stepik.org/lesson/236895/step/1',
'https://stepik.org/lesson/236896/step/1',
'https://stepik.org/lesson/236897/step/1',
'https://stepik.org/lesson/236898/step/1',
'https://stepik.org/lesson/236899/step/1',
'https://stepik.org/lesson/236903/step/1',
'https://stepik.org/lesson/236904/step/1',
'https://stepik.org/lesson/236905/step/1']
message = ''

class TestStepik():
    def test_signin_check(self, browser):
        browser.get(link1)
        signin_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, 'ember33'))) # id 'ember33'
        signin_button.click()

        # найти объект с классом .modal-dialog-inner,
        email_input = browser.find_element(By.ID, 'id_login_email')
        email_input.send_keys(login)

        password_input = browser.find_element(By.ID, 'id_login_password')
        password_input.send_keys(password)

        submit = browser.find_element(By.CSS_SELECTOR, '.sign-form__btn.button_with-loader')
        submit.click()
    @pytest.mark.parametrize('link_parts', link_list)
    def test_answer_spam(self, browser, link_parts):
        link2 = link_parts
        answer = math.log(int((time.time())))
        browser.get(link2)
        answer_input = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'textarea:required')))
        answer_input.send_keys(str(answer))
        submit_button = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.submit-submission'))
        )
        submit_button.click()

        feedback = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".smart-hints.ember-view.lesson__hint p")))
        feedback_text = feedback.text
        assert 'Correct!' in feedback_text
if __name__ == '__main__':
    pytest.main()