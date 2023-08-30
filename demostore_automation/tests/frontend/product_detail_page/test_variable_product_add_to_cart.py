
import pytest
import logging as logger
from demostore_automation.src.pages.ProductPage import ProductPage
from demostore_automation.src.pages.CartPage import CartPage

# test data
# hard coding a product that has these variables (color & logo)
PRODUCT_SLUG = 'hoodie'

@pytest.mark.feregression
@pytest.mark.fesmoke
@pytest.mark.usefixtures("init_driver")
class TestVariableProductAddToCartPDP:

    @pytest.mark.tcid301
    def test_variable_product_pdp_select_options_add_to_cart(self):
        """
           Test the functionality of adding a variable product with selected options to the cart.

           This function navigates to a product page for a variable product, selects specific color and logo options,
           adds the product to the cart, goes to the cart page, and verifies that the item has been added to the cart.

           Args:
               self (object): The test case or test suite instance.

           Returns:
               None
           """

        logger.info("Testing 'add to cart' functionality for a variable product...")

        # test data
        color_to_select = 'Blue'
        logo_to_select = 'Yes'
        expected_text = 'Hoodie - Blue, Yes'

        # go to product page for a variable product
        product_page = ProductPage(self.driver)
        product_page.go_to_product_page(PRODUCT_SLUG)

        # select a color
        product_page.select_color_option_and_verify(color_to_select)

        # select a logo
        product_page.select_logo_option_and_verify(logo_to_select)

        # click add to cart
        product_page.click_add_to_cart_button()

        # go to cart
        product_page.go_to_cart_page()

        # verify cart page has loaded
        cart_page = CartPage(self.driver)
        cart_page.click_apply_coupon()

        # verify items are in cart
        cart_page.verify_item_in_cart_by_visible_text(expected_text)
