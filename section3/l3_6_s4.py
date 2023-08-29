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
login = r''
password = ''

class TestStepik():
    alien_message = ''
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
    @pytest.mark.parametrize('link_parts', list(range(895, 900)) + list(range(903, 906)))
    def test_answer_spam(self, browser, link_parts):
        link2 = f'https://stepik.org/lesson/236{link_parts}/step/1'
        browser.get(link2)
        answer_input = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'textarea:required'))) # id 'ember93'
        answer_input.clear()
        answer = math.log(int((time.time())))
        answer_input.send_keys(answer)
        submit = browser.find_element(By.CSS_SELECTOR, '.submit-submission')
        submit.click()

        feedback = browser.find_element(By.CSS_SELECTOR, 'p.smart-hints__hint')
        feedback_text = feedback.text
        if feedback_text != 'Correct!':
            self.alien_message += feedback_text
        # assert 'Correct!' in feedback_text
    print(alien_message)