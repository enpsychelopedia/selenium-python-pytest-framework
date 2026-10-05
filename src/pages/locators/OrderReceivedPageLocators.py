

from selenium.webdriver.common.by import By

class OrderReceivedPageLocators: 

    ORDER_RECEIVED_MESSAGE = (By.CSS_SELECTOR, 'p.woocommerce-thankyou-order-received')

    ORDER_NUMBER = (By.CSS_SELECTOR, 'li.woocommerce-order-overview__order strong')