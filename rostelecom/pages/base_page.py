import os
import requests
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.presence_of_element_located(locator))

    def find_element(self, locator, time=10):
        element = WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator)
        )
        return element

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def wait_for_element(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        element = wait.until(EC.presence_of_element_located(locator))
        return element

    def wait_for_elements(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        elements = wait.until(EC.presence_of_all_elements_located(locator))
        return elements
