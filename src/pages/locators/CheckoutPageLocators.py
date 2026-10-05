

from selenium.webdriver.common.by import By

class CheckoutPageLocators:

    EMAIL_ADDRESS_FIELD = (By.ID, 'email')
    F_NAME_FIELD = (By.ID, 'billing-first_name')
    L_NAME_FIELD = (By.ID, 'billing-last_name')
    STREET_AD_FIELD = (By.ID, 'billing-address_1')
    TOWN_FIELD = (By.ID, 'billing-city')
    POSTC_FIELD = (By.ID, 'billing-postcode')

    PLACE_ORDER_BTN = (By.CSS_SELECTOR, 'button.wc-block-components-checkout-place-order-button')