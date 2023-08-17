
from selenium.webdriver.common.by import By

class ProductPageLocators:

    VARIABLE_PRODUCT_COLOR_ATTRIBUTE_DROPDOWN = (By.ID, 'pa_color')
    VARIABLE_PRODUCT_LOGO_ATTRIBUTE_DROPDOWN = (By.ID, 'logo')
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, 'div[class*="add-to-cart"] button[class*=add_to_cart_button][type="submit"]')
    GO_TO_CART_PAGE = (By.CSS_SELECTOR, '#site-header-cart li a[class="cart-contents"]')

