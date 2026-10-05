

from seleframework.src.SeleniumExtended import SeleniumExtended
from seleframework.src.pages.locators.HeaderLocators import HeaderLocators

class Header(HeaderLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def verify_cart_item_count(self, count):
        self.sl.wait_for_item_count(self.CART_ITEM_COUNT_LOCATOR, count)

    def click_on_cart(self):
        self.sl.wait_and_click(self.CART_LOCATOR)