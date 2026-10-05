

from seleframework.src.SeleniumExtended import SeleniumExtended
from seleframework.helpers.config_helpers import get_base_url
from seleframework.src.pages.locators.MyAccountSignedOutLocators import MyAccountSignedOutLocators

class MyAccountSignedOut(MyAccountSignedOutLocators):

    endpoint = '/my-account/'

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_my_account(self):
        base_url = get_base_url()
        my_account_url = base_url + self.endpoint
        self.driver.get(my_account_url)

    def register_email_address(self, email):
        self.sl.wait_and_input_text(self.REGISTER_EMAIL_FIELD_LOCATOR, email)

    def register_password(self, password):
        self.sl.wait_and_input_text(self.REGISTER_PASSWORD_FIELD_LOCATOR, password)

    def click_register_btn(self):
        self.sl.wait_and_click(self.REGISTER_BTN_LOCATOR)

    def input_email_address(self, email):
        self.sl.wait_and_input_text(self.USERNAME_FIELD_LOCATOR, email)

    def input_password(self, password):
        self.sl.wait_and_input_text(self.PASSWORD_FIELD_LOCATOR, password)

    def click_login_btn(self):
        self.sl.wait_and_click(self.LOGIN_BTN_LOCATOR)

    def get_error_message(self):
        error_message = self.sl.wait_and_get_error_message(self.ERROR_MESSAGE)
        return error_message 