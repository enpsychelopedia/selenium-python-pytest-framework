

from seleframework.src.SeleniumExtended import SeleniumExtended
from seleframework.src.pages.locators.MyAccountSignedInLocators import MyAccountSignedInLocators

class MyAccountSignedIn(MyAccountSignedInLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def verify_logout_btn_is_visible(self):
        self.sl.wait_for_element_to_be_visible(self.LOG_OUT_BTN_LOCATOR)
        return True