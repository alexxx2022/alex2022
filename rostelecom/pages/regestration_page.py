# registration_page.py

from selenium.webdriver.common.by import By


class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.XPATH, "[name='username']")
        self.email_input = (By.CSS_SELECTOR, "[name='email']")
        self.password_input = (By.CSS_SELECTOR, "[name='password']")
        self.submit_button = (By.CSS_SELECTOR, "[type='submit']")

    def open(self):
        self.driver.get(
            "https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration?client_id=account_b2c&tab_id=-d-xfDV51X8")

    def input_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    def input_email(self, email):
        self.driver.find_element(*self.email_input).send_keys(email)

    def input_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)
        time.sleep(5)

    def submit(self):
        self.driver.find_element(*self.submit_button).click()
