from selenium.webdriver.common.by import By

class LoginPageLocators:
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")
    ERROR_MESSAGE = (By.XPATH, "//div[@class='kc-feedback-text']")
    PASSWORD_RESET_LINK = (By.LINK_TEXT, "Забыли пароль?")
    REGISTER_LINK = (By.LINK_TEXT, "Зарегистрироваться")
