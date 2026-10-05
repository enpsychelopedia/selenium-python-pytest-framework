

from seleframework.src.SeleniumExtended import SeleniumExtended
from seleframework.src.pages.locators.CartPageLocators import CartPageLocators

class CartPage(CartPageLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def get_cart_item_names(self):
        elements = self.sl.wait_and_get_elements(self.CART_ITEMS)
        return [element.text for element in elements]

    def click_add_coupon_dropdown(self):
        self.sl.wait_and_click(self.ADD_COUPON_DROPDOWN_LOCATOR)

    def enter_coupon_code(self, coupon_code):
        self.sl.wait_and_input_text(self.ENTER_CODE_FIELD_LOCATOR, coupon_code)

    def click_apply_btn(self):
        self.sl.wait_and_click(self.APPLY_BTN)

    def verify_estimated_total(self):
        total = self.sl.wait_and_get_text(self.TOTAL_TEXT_LOCATOR)
        return total

    def add_coupon_code(self, coupon_code):
        self.get_cart_item_names()
        self.click_add_coupon_dropdown()
        self.enter_coupon_code(coupon_code)
        self.click_apply_btn()
        total = self.verify_estimated_total()
        assert  total == "₱0.00", f"Coupon wasn't applied. Estimated total: {total}"

    def proceed_to_checkout(self):
        self.sl.wait_and_click(self.PROCEED_TO_CHECKOUT_BTN)