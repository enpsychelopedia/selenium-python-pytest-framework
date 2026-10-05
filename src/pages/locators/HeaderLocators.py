

from selenium.webdriver.common.by import By

class HeaderLocators: 

    CART_ITEM_COUNT_LOCATOR = (By.CSS_SELECTOR, 'a.cart-contents span.count')
    CART_LOCATOR = (By.CSS_SELECTOR, 'a.cart-contents')