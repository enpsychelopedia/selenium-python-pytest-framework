

from seleframework.src.SeleniumExtended import SeleniumExtended
from seleframework.src.pages.locators.OrderReceivedPageLocators import OrderReceivedPageLocators

class OrderReceivedPage(OrderReceivedPageLocators): 

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def verify_order_received(self):
        return self.sl.wait_and_get_text(self.ORDER_RECEIVED_MESSAGE)

    def get_order_number(self):
        return self.sl.wait_and_get_text(self.ORDER_NUMBER)