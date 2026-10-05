

from seleframework.helpers.config_helpers import get_base_url
from seleframework.src.pages.locators.HomepageLocators import HomepageLocators
from seleframework.src.SeleniumExtended import SeleniumExtended

class HomePage(HomepageLocators): 

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_homepage(self):
        homepage_url = get_base_url()
        self.driver.get(homepage_url)

    def add_first_item_to_cart(self):
        self.sl.wait_and_click(self.FIRST_ADD_TO_CART_BTN)
