


import pytest
from seleframework.src.pages.MyAccountSignedOut import MyAccountSignedOut
from seleframework.helpers.generic_helpers import generate_random_email_and_password

@pytest.mark.usefixtures("init_driver")
class TestInvalidUser:

    @pytest.mark.tcid2
    def test_invalid_user(self):

        my_account = MyAccountSignedOut(self.driver)

        my_account.go_to_my_account()

        rand_info = generate_random_email_and_password()
        my_account.input_email_address(rand_info["email"])
        my_account.input_password(rand_info["password"])
        my_account.click_login_btn()

        error_message = "Unknown email address. Check again or try your username."
        actual_err = my_account.get_error_message()
        assert error_message == actual_err, f"Unexpected error: {actual_err}"