from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from pages.login_page import LoginPage

def test_site_status_code():
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    login_page.open()
    assert driver.current_url == login_page.url
    driver.quit()

def test_site_redirect():
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    login_page.open()
    assert driver.current_url == login_page.url
    driver.quit()

def test_form_input():
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    login_page.open()
    login_page.input_username("uddinmecardopw.h.t.2.3.0.4@gmail.com")
    login_page.input_password("Gjitkyf[eq")
    login_page.submit_form()
    assert driver.current_url != login_page.url
    driver.quit()
def test_invalid_username_input():
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    login_page.open()
    login_page.input_username("invalid_username")
    login_page.input_password("Gjitkyf[eq")
    login_page.submit_form()
    
    error_message = login_page.get_error_message()
    assert error_message == "Неверный логин или пароль"
    driver.quit()

def test_invalid_password_input():
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    login_page.open()
    login_page.input_username("uddinmecardopw.h.t.2.3.0.4@gmail.com")
    login_page.input_password("invalid_password")
    login_page.submit_form()
    error_message = login_page.get_error_message()
    assert error_message == "Неверный логин или пароль"
    driver.quit()

def test_empty_form_submission():
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    login_page.open()
    login_page.submit_form()
    error_message = login_page.get_error_message()
    assert error_message == "Введите логин и пароль"
    driver.quit()
def test_remember_me_feature():
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    login_page.open()
    login_page.input_username("test_user")
    login_page.input_password("test_password")
    login_page.click_remember_me()
    login_page.submit_form()
    login_page.open()
    assert login_page.is_username_field_populated() == True
    assert login_page.is_remember_me_checked() == True
    driver.quit()
def test_form_elements_visibility():
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    login_page.open()
    assert login_page.is_username_input_field_visible() == True
    assert login_page.is_password_input_field_visible() == True
    assert login_page.is_submit_button_visible() == True
    driver.quit()

def test_form_elements_enabling():
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    login_page.open()
    assert login_page.is_username_input_field_enabled() == True
    assert login_page.is_password_input_field_enabled() == True
    assert login_page.is_submit_button_enabled() == True
    driver.quit()

def test_form_input_field_types():
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    login_page.open()
    assert login_page.get_username_input_field_type() == "Почта"
    assert login_page.get_password_input_field_type() == "Пароль"
    driver.quit()

def test_form_element_placeholder_text():
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    login_page.open()
    assert login_page.get_username_input_field_placeholder_text() == "Электронная почта"
    assert login_page.get_password_input_field_placeholder_text() == "Пароль"
    driver.quit()
def test_form_element_labels():
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    login_page.open()
    assert login_page.get_username_input_field_label() == "Логин"
    assert login_page.get_password_input_field_label() == "Пароль"
    driver.quit()

def test_successful_login():
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("valid_username", "valid_password")
    assert login_page.is_logged_in() == True
    driver.quit()
def test_password_input():
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    login_page.open()
    login_page.input_password("my_secret_password")
    password_input = login_page.get_password_input()
    assert password_input.get_attribute("value") == "my_secret_password"

def test_login_button():
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    login_page.open()
    login_button = login_page.get_login_button()
    assert login_button.is_displayed()
    login_button.click()
