

import pytest
from seleframework.src.pages.Homepage import HomePage
from seleframework.src.pages.Header import Header
from seleframework.src.pages.CartPage import CartPage
from seleframework.configs.generic_configs import GenericConfigs
from seleframework.src.pages.CheckoutPage import CheckoutPage
from seleframework.src.pages.OrderReceivedPage import OrderReceivedPage
from seleframework.helpers.database_helper import get_order_no_from_db

@pytest.mark.usefixtures("init_driver")
class TestEndToEndCheckoutGuestUser:

    @pytest.mark.tcid3
    def test_end_to_end_checkout_guest_user(self):

        home_p = HomePage(self.driver)
        header_p = Header(self.driver)
        cart_p = CartPage(self.driver)
        checkout_p = CheckoutPage(self.driver)
        order_received_p = OrderReceivedPage(self.driver)

        home_p.go_to_homepage()
        home_p.add_first_item_to_cart()

        # choose product and go to cart
        header_p.verify_cart_item_count(1)
        header_p.click_on_cart()

        # cart
        cart_count = cart_p.get_cart_item_names()
        assert len(cart_count) == 1, f"Cart item count not as expected. Cart contains: {cart_count}"

        # enter coupon code
        coupon_code = GenericConfigs.FREE_COUPON_CODE
        cart_p.add_coupon_code(coupon_code)

        # proceed to checkout
        cart_p.proceed_to_checkout() 

        # fill checkout information 
        checkout_p.fillout_billing_info()

        # place order
        checkout_p.place_order()

        # order received / confirmationm 
        order_received_page_msg = order_received_p.verify_order_received()
        assert order_received_page_msg == "Thank you. Your order has been received.", f"Unexpected order confirmation message: {order_received_page_msg}"

        # verify order was successful
        order_no = order_received_p.get_order_number()
        print(f"Order placement success! Order no:{order_no}")

        assert get_order_no_from_db(order_no), "Order was not found in db after placing."

