


from seleframework.src.SeleniumExtended import SeleniumExtended
from seleframework.helpers.generic_helpers import generate_random_email_and_password
from seleframework.src.pages.locators.CheckoutPageLocators import CheckoutPageLocators

class CheckoutPage(CheckoutPageLocators): 

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def input_email_address(self, email=None):
        rand_info = generate_random_email_and_password()

        email = email if email else rand_info["email"]
        self.sl.wait_and_input_text(self.EMAIL_ADDRESS_FIELD, email)

    def input_first_name(self, f_name=None):
        f_name = f_name if f_name else "Test"

        self.sl.wait_and_input_text(self.F_NAME_FIELD, f_name)

    def input_last_name(self, l_name=None):
        l_name = l_name if l_name else "User"

        self.sl.wait_and_input_text(self.L_NAME_FIELD, l_name)

    def input_street_ad(self, st_address=None):
        st_address = st_address if st_address else "123 Main St."

        self.sl.wait_and_input_text(self.STREET_AD_FIELD, st_address)

    def input_town_name(self, town=None):
        town = town if town else "Sunshine Town"

        self.sl.wait_and_input_text(self.TOWN_FIELD, town)

    def input_postcode(self, postcode=None):
        postcode = postcode if postcode else 1234

        self.sl.wait_and_input_text(self.POSTC_FIELD, postcode)

    def fillout_billing_info(self, email=None, f_name=None, l_name=None, st_address=None, town=None, postcode=None):

        self.input_email_address(email)
        self.input_first_name(f_name)
        self.input_last_name(l_name)
        self.input_street_ad(st_address)
        self.input_town_name(town)
        self.input_postcode(postcode)

    def place_order(self):
        self.sl.wait_and_click(self.PLACE_ORDER_BTN)