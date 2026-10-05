


from selenium.webdriver.common.by import By

class MyAccountSignedOutLocators:

    REGISTER_EMAIL_FIELD_LOCATOR = (By.ID, "reg_email")
    REGISTER_PASSWORD_FIELD_LOCATOR = (By.ID, "reg_password")
    REGISTER_BTN_LOCATOR = (By.CSS_SELECTOR, 'button.woocommerce-form-register__submit')

    USERNAME_FIELD_LOCATOR = (By.ID, 'username')
    PASSWORD_FIELD_LOCATOR = (By.ID, 'password')
    LOGIN_BTN_LOCATOR = (By.CSS_SELECTOR, 'button.woocommerce-form-login__submit')

    ERROR_MESSAGE = (By.CSS_SELECTOR, 'ul.woocommerce-error li')