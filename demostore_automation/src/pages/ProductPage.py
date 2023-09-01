

from demostore_automation.src.selenium_extended.SeleniumExtended import SeleniumExtended
from demostore_automation.src.configs.MainConfigs import MainConfigs
from demostore_automation.src.pages.locators.ProductPageLocators import ProductPageLocators
from selenium.webdriver.support.ui import Select


class ProductPage(ProductPageLocators):
    endpoint = '/product/'

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(driver)

    def go_to_product_page(self, product_slug):
        base_url = MainConfigs.get_base_url()
        product_url = base_url + self.endpoint + product_slug
        self.driver.get(product_url)

    def select_color_option_and_verify(self, color_to_select):
        # select the dropdown
        self.select_color_option_by_visible_text(color=color_to_select)

        # verify it is selected
        selected_element = self.get_selected_color_option()
        selected_text = selected_element.text
        assert color_to_select == selected_text, f"Expected to select '{selected_element}' from dropdown but actual" \
                                                 f"selected was '{selected_text}'."

    def select_logo_option_and_verify(self, logo_to_select):
        # select the dropdown
        self.select_logo_option_by_visible_text(logo=logo_to_select)

        # verify it is selected
        selected_element = self.get_selected_logo_option()
        selected_text = selected_element.text
        assert logo_to_select == selected_text, f"Expected to select '{selected_element}' from dropdown but actual" \
                                                 f"selected was '{selected_text}'."

    def select_color_option_by_visible_text(self, color):
        self.sl.wait_and_select_dropdown(self.VARIABLE_PRODUCT_COLOR_ATTRIBUTE_DROPDOWN, color)

    def select_logo_option_by_visible_text(self, logo):
        self.sl.wait_and_select_dropdown(self.VARIABLE_PRODUCT_LOGO_ATTRIBUTE_DROPDOWN, logo)

    def get_selected_color_option(self):
        color_dropdown_elem = self.sl.wait_until_element_is_visible(self.VARIABLE_PRODUCT_COLOR_ATTRIBUTE_DROPDOWN)
        select = Select(color_dropdown_elem)
        selected_element = select.first_selected_option
        return selected_element

    def get_selected_logo_option(self):
        logo_dropdown_elem = self.sl.wait_until_element_is_visible(self.VARIABLE_PRODUCT_LOGO_ATTRIBUTE_DROPDOWN)
        select = Select(logo_dropdown_elem)
        selected_element = select.first_selected_option
        return selected_element

    def click_add_to_cart_button(self):
        self.sl.wait_and_click(self.ADD_TO_CART_BUTTON)

    def go_to_cart_page(self):
        self.sl.wait_and_click(self.GO_TO_CART_PAGE)
