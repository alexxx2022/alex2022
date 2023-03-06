# test_registration_page.py

from selenium import webdriver

from locators import locators
from locators.locators import LoginPageLocators
from pages.login_page import LoginPage
from pages.regestration_page import RegistrationPage


class TestRegistration:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.registration_page = RegistrationPage(self.driver)
        self.registration_page.open()

    def teardown_method(self):
        self.driver.quit()

    def test_registration(self):
        self.registration_page.input_username("test_username")
        self.registration_page.input_email("test_email@example.com")
        self.registration_page.input_password("test_password")
        self.registration_page.submit()
        time.sleep(5) 

def test_login_form_is_displayed():
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    login_page.open()
    assert login_page.is_form_displayed() == True
    driver.quit()

def test_login_form_input_username():
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    
    login_page.open()
    login_page.input_username("test_username")
    assert login_page.driver.find_element(*LoginPageLocators.USERNAME_INPUT).get_attribute("value") == "test_username"
    driver.quit()

def test_login_form_input_password():
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    login_page.open()
    login_page.input_password("test_password")
    assert login_page.driver.find_element(*LoginPageLocators.PASSWORD_INPUT).get_attribute("value") == "test_password"
    driver.quit()
    time.sleep(5) 

def test_form_submit_with_empty_username_and_password():
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    login_page.open()
    login_page.submit()
    error_message = login_page.get_error_message()
    assert error_message == "Необходимо заполнить поле Имя пользователя или Электронная почта."
    driver.quit()
    time.sleep(5) 

def test_form_submit_with_empty_username():
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    login_page.open()
    login_page.input_password("test_password")
    login_page.submit()
    error_message = login_page.get_error_message()
    assert error_message == "Необходимо заполнить поле Имя пользователя или Электронная почта."
    driver.quit()

def test_form_submit_with_empty_password():
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    login_page.open()
    login_page.input_username("test_username")
    login_page.submit_form()
    error_message = login_page.get_error_message()
    assert error_message == "Password is required"
    driver.quit()
    time.sleep(5) 

def test_form_submit_with_empty_username():
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    login_page.open()
    login_page.input_password("test_password")
    login_page.submit_form()
    error_message = login_page.get_error_message()
    assert error_message == "Username is required"
    driver.quit()

def test_form_submit_with_incorrect_username_password():
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    login_page.open()
    login_page.input_username("incorrect_username")
    login_page.input_password("incorrect_password")
    login_page.submit_form()
    error_message = login_page.get_error_message()
    assert error_message == "Invalid username or password"
    driver.quit()
    time.sleep(5) 

def test_form_submit_with_correct_username_password():
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    login_page.open()
    login_page.input_username("correct_username")
    login_page.input_password("correct_password")
    login_page.submit_form()
    assert login_page.driver.current_url == "https://b2c.passport.rt.ru/account_b2c/login_success"
    driver.quit()

def test_form_remember_me_functionality():
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    login_page.open()
    login_page.input_username("correct_username")
    login_page.input_password("correct_password")
    login_page.remember_me()
    login_page.submit_form()
    assert login_page.is_remember_me_selected() == True
    driver.quit()
    time.sleep(5) 

def test_form_forgot_password_link():
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    login_page.open()
    login_page.click_forgot_password_link()
    assert login_page.driver.current_url == "https://b2c.passport.rt.ru/account_b2c/forgot_password"
    driver.quit()
    time.sleep(5) 
    
def test_form_submit_with_empty_password(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.input_username("test_username")
    login_page.password_input.submit()

    error_message = login_page.driver.find_element(*locators.PASSWORD_ERROR_MESSAGE)
    assert error_message.is_displayed()
    assert error_message.text == "Please enter your password."
def test_form_submit_with_empty_username(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.input_password("test_password")
    login_page.password_input.submit()

    error_message = login_page.driver.find_element(*locators.USERNAME_ERROR_MESSAGE)
    assert error_message.is_displayed()
    assert error_message.text == "Please enter your username."
