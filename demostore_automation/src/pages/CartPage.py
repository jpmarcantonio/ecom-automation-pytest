

from demostore_automation.src.selenium_extended.SeleniumExtended import SeleniumExtended
from demostore_automation.src.pages.locators.CartPageLocators import CartPageLocators
from demostore_automation.src.configs.MainConfigs import MainConfigs


class CartPage(CartPageLocators):

    endpoint = '/cart'

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(driver)

    def go_to_cart_page(self):
        base_url = MainConfigs.get_base_url()
        cart_url = base_url + self.endpoint
        self.driver.get(cart_url)

    def get_all_product_names_in_cart(self):
        product_name_elements = self.sl.wait_and_get_elements(self.PRODUCT_NAMES_IN_CART)
        product_names = [i.text for i in product_name_elements]
        # product_names = []
        # for i in product_name_elements:
        #     product_names.append(i.text)
        return product_names

    def input_coupon(self, coupon_code):
        self.sl.wait_and_input_text(self.COUPON_FIELD, str(coupon_code))

    def click_apply_coupon(self):
        self.sl.wait_and_click(self.APPLY_COUPON_BTN, timeout=10)

    def apply_coupon(self, coupon_code):
        self.input_coupon(coupon_code)
        self.click_apply_coupon()

    def click_on_proceed_to_checkout(self):
        self.sl.wait_and_click(self.PROCEED_TO_CHECKOUT_BTN)

    def verify_coupon_error_message(self, exp_err):
        self.sl.wait_until_element_contains_text(self.COUPON_ERROR_MSG, exp_err)

    def verify_item_in_cart_by_visible_text(self, exp_text):
        self.sl.wait_until_element_contains_text(self.PRODUCT_NAMES_IN_CART, exp_text)
