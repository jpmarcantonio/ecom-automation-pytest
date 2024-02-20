
from demostore_automation.src.utilities.wooAPIUtility import WooAPIUtility

class ProductsReviewsAPIHelper:


    def __init__(self):
        self.woo_api_utility = WooAPIUtility()

    def call_create_product_review(self, payload, expected_status_code):
       return self.woo_api_utility.post("products/reviews", params=payload, expected_status_code=expected_status_code)