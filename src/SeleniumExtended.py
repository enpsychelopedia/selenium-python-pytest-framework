

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SeleniumExtended:

    def __init__(self, driver):
        self.driver = driver
        self.default_timeout = 10

    def wait_and_input_text(self, locator, text, timeout=None):
        timeout = timeout if timeout else self.default_timeout

        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        ).send_keys(text)

    def wait_and_click(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout

        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        ).click()

    def wait_for_element_to_be_visible(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout

        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_and_get_error_message(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout

        error_message = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        
        return error_message.text

    def wait_for_item_count(self, locator, count, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        count = str(count) + " item"

        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(locator, count)
        )

    def wait_and_get_elements(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout

        elements = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_all_elements_located(locator)
        )

        return elements

    def wait_and_get_text(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout

        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

        return element.text