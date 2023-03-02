from datetime import datetime
import pytest
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield driver
    attach = driver.get_screenshot_as_png()
    driver.quit()
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def login_page():
    url = "https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=9ec8fcb4-74f4-4a25-8ba3-4c7252919961&theme&auth_type"
    response = requests.get(url)
    return response

def test_login(driver, login_page):
    driver.get(login_page.url)
    login = LoginPage(driver)
    login.enter_username("testuser")
    login.enter_password("testpassword")
    login.submit()
    assert "Successful Login" in driver.page_source
    assert login_page.status_code == 200
