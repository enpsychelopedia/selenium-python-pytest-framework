


import pytest
from seleframework.src.pages.MyAccountSignedOut import MyAccountSignedOut
from seleframework.src.pages.MyAccountSignedIn import MyAccountSignedIn
from seleframework.helpers.generic_helpers import generate_random_email_and_password

@pytest.mark.usefixtures("init_driver")
class TestRegisterNewUser: 

    @pytest.mark.tcid1
    def test_register_new_user(self):

        my_account_signed_out = MyAccountSignedOut(self.driver)
        my_account_signed_in = MyAccountSignedIn(self.driver)

        my_account_signed_out.go_to_my_account()

        rand_info = generate_random_email_and_password()
        my_account_signed_out.register_email_address(rand_info["email"])
        my_account_signed_out.register_password(rand_info["password"])

        my_account_signed_out.click_register_btn()

        is_logged_in = my_account_signed_in.verify_logout_btn_is_visible()
        assert is_logged_in, "User was not logged in after registration."
