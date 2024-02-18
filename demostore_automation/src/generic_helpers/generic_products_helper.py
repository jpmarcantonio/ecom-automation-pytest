
from demostore_automation.src.utilities.genericUtilities import generate_random_string
from demostore_automation.src.api_helpers.ProductsAPIHelper import ProductsAPIHelper


class  GenericProductsHelper:

    def __init__(self):
        self.products_api_helper = ProductsAPIHelper()

    def create_a_product(self, product_name=None, type='simple'):
        payload = dict()
        if product_name == None:
            rand_str = generate_random_string(20)
            # payload = dict()
            payload['name'] = rand_str
        else:
            payload['name'] = product_name

        payload['type'] = type

        # todo: implement assertion error to check that user's given product type is valid. Options: simple, grouped, external and variable.

        rs_api = self.products_api_helper.call_create_product(payload=payload, expected_status_code=201)

        return rs_api

    def get_product_detail_via_api(self, product_id):
        return self.products_api_helper.call_get_product_py_id(product_id)
