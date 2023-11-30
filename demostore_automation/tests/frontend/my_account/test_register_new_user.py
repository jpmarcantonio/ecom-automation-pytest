

import pytest
from demostore_automation.src.pages.MyAccountSignedOutPage import MyAccountSignedOutPage
from demostore_automation.src.pages.MyAccountSignedInPage import MyAccountSignedInPage
from demostore_automation.src.utilities.genericUtilities import generate_random_email_and_password


pytestmark = [pytest.mark.feregression, pytest.mark.fesmoke, pytest.mark.my_account]



@pytest.mark.usefixtures("init_driver")
class TestRegisterNewUser:


    @pytest.mark.tcid13
    @pytest.mark.pioneertcid2
    @pytest.mark.edf70
    def test_register_valid_new_user(self):
        """
        Test to verify a valid user can register to the site.
        It generates a random email and password, then registers the user.
        It then logs out of the registered user's account.
        :return:
        """
        # create objects
        myacct = MyAccountSignedOutPage(self.driver)
        myacct_sin = MyAccountSignedInPage(self.driver)

        # go to my account page
        myacct.go_to_my_account()

        random_info = generate_random_email_and_password()
        # fill in the username for registration
        myacct.input_register_email(random_info['email'])

        # fill in the password for registration
        myacct.input_register_password(random_info['password'])

        # click on 'register'
        myacct.click_register_button()

        # verify user is registered
        myacct_sin.verify_user_is_signed_in()

        # logout
        myacct_sin.logout_user()

    @pytest.mark.edf57
    def test_register_user_failure_email_only(self):
        """
        Test to verify that a user cannot be registered using only an email address. The test navigates to the My account
        page, generates a random email address, then attempts to register the user without filling in the password field.
        :return:
        """
        # create objects
        myacct = MyAccountSignedOutPage(self.driver)
        exp_err = "Please enter an account password."

        # go to my account page
        myacct.go_to_my_account()

        # generate random email
        random_info = generate_random_email_and_password()

        # fill in email field for registration
        myacct.input_register_email(random_info['email'])

        # click on 'register'
        myacct.click_register_button()

        # verify user is not registered
        myacct.wait_until_error_is_displayed(exp_err)

    @pytest.mark.edf59
    def test_register_user_failure_password_only(self):
        """
        Test to verify that a user cannot register using only a password. The test navigates to the My account page,
        generates a random password, and attempts to register the user without filling in the email field.
        :return:
        """
        # create objects
        myacct = MyAccountSignedOutPage(self.driver)
        exp_err = 'Please provide a valid email address.'

        # navigate to my account page
        myacct.go_to_my_account()

        # generate random password
        random_info = generate_random_email_and_password()

        # fill in the password field for registration
        myacct.input_register_password(random_info['password'])

        # click 'register'
        myacct.click_register_button()

        # verify register user failure
        myacct.wait_until_error_is_displayed(exp_err)

    @pytest.mark.edf58
    def test_register_user_failure_no_email_no_password(self):
        """
        Test to verify that a user cannot register without providing an email address or password. The test navigates to
        the My account page and attempts to register a user without filling in the email or password field.
        :return:
        """
        # create objects
        myacct = MyAccountSignedOutPage(self.driver)
        exp_err = 'Please provide a valid email address.'

        # navigate to my account page
        myacct.go_to_my_account()

        # click 'register'
        myacct.click_register_button()

        # verify register failure
        myacct.wait_until_error_is_displayed(exp_err)