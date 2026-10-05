

from selenium.webdriver.common.by import By

class CartPageLocators:

    CART_ITEMS = (By.CSS_SELECTOR, 'tr.wc-block-cart-items__row  a.wc-block-components-product-name')

    ADD_COUPON_DROPDOWN_LOCATOR = (By.CSS_SELECTOR, 'div.wc-block-components-panel__button')
    ENTER_CODE_FIELD_LOCATOR = (By.ID, 'wc-block-components-totals-coupon__input-coupon')
    APPLY_BTN = (By.CSS_SELECTOR, 'button.wc-block-components-totals-coupon__button')

    TOTAL_TEXT_LOCATOR = (By.CSS_SELECTOR, 'div.wc-block-components-totals-item__value span')
    PROCEED_TO_CHECKOUT_BTN = (By.CSS_SELECTOR, 'div.wc-block-components-button__text')