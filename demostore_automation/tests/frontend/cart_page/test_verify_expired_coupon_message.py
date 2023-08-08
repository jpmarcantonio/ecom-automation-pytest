
import pytest

from demostore_automation.src.pages.HomePage import HomePage
from demostore_automation.src.pages.CartPage import CartPage
from demostore_automation.src.pages.Header import Header
from demostore_automation.src.configs.MainConfigs import MainConfigs


pytestmark = [pytest.mark.feregression, pytest.mark.fesmoke, pytest.mark.cart_page]

@pytest.mark.usefixtures("init_driver")
class TestVerifyExpiredCouponMessage:

    @pytest.mark.tcid300
    def test_verify_expired_coupon_message(self):
        #create obejcts
        home_page = HomePage(self.driver)
        header = Header(self.driver)
        cart_page = CartPage(self.driver)

        # go to home page
        home_page.go_to_home_page()

        # add item to cart page
        home_page.click_first_add_to_cart_button()

        # Verify cart is updated before navigating to cart page
        header.wait_until_cart_item_count(1)

        # Navigate to cart page
        header.click_on_cart_on_right_header()

        # input and apply expired coupon code
        coupon_code = MainConfigs.get_coupon_code("EXPIRED_COUPON")
        cart_page.apply_coupon(coupon_code)

        # Verify error message is displayed on cart page and text is correct
        expected_error_msg = 'This coupon has expired.'
        cart_page.verify_coupon_error_message(expected_error_msg)



