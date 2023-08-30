
import logging as logger
import json
import os.path
from demostore_automation.src.api_helpers.OrdersAPIHelper import OrdersAPIHelper
from demostore_automation.src.dao.orders_dao import OrdersDAO
from demostore_automation.src.dao.products_dao import ProductsDAO


class GenericOrderHelper:

    def __init__(self):
        self.order_api_helper = OrdersAPIHelper()
        self.cur_file_dir = os.path.dirname(os.path.realpath(__file__))
        self.product_dao = ProductsDAO

    def create_order(self, additional_args=None):
        """
          Create an order using the provided payload and additional arguments.

          This function creates an order using a pre-defined JSON payload template loaded from a file. If additional
          arguments are provided, they are merged with the payload. If the additional arguments do not contain line
          items information, a random product is selected from the database and added as a line item to the order payload.

          Args:
              self (object): The instance of the class containing this method.
              additional_args (dict, optional): Additional arguments to merge with the order payload. If provided, it should
                  be a dictionary containing keys and values to be added or updated in the order payload.

          Returns:
              dict: A dictionary containing the response from the order API after attempting to create the order.
          """

        payload_template = os.path.join(self.cur_file_dir, '..', 'data', 'create_order_payload.json')
        with open(payload_template, 'r') as f:
            order_payload = json.load(f)

        if additional_args:
            assert isinstance(additional_args, dict), f"the parameter 'additional_args' must be type dictionary."
            order_payload.update(additional_args)

        # if additional_args (passed in argument) does not have line items then add line items to the payload
        if additional_args and "line_items" not in additional_args.keys():
            rand_product = self.product_dao.get_random_product_from_db(qty=1)
            rand_product_id = rand_product['0']['ID']
            order_payload["line_items"] = [{"product_id": rand_product_id, "quantity": 1}]

        response_create_order = self.order_api_helper.call_create_order(payload=order_payload)

        return response_create_order

    def verify_order_is_created(self, order_json, exp_cust_id, exp_products):
        """
        Verifies that an order is created as expected.

        :param order_json: The JSON response representing the created order.
        :type order_json: dict
        :param exp_cust_id: The expected customer ID for the created order.
        :param exp_cust_id: int
        :param exp_products: a list of dictionaries. Example: [{'product_id': product_id}]
        :return:
        :raises AssertionError: If any verification checks fail.
        """

        logger.debug(f"Verifying order is created.")

        # get the order id from the json
        order_id = order_json['id']

        # verify the api response object is not empty
        assert order_json, f"Create order response is empty."

        # verify expected customer id
        assert order_json['customer_id'] == exp_cust_id, f"Create order with given customer id returned bad customer id." \
                                                         f"Expected customer_id={exp_cust_id}, but got {order_json['customer_id']}."

        # verify number of products in api response is as expected
        assert len(order_json['line_items']) == len(exp_products), f"Expected only {len(exp_products)} items in order but " \
                                                                   f"found '{len(order_json['line_items'])}'." \
                                                                   f"Order id: {order_json['id']}."

        # add additional verification: write logic to check item ids. Loop through line items in order_json and check ids.

        # verify db
        order_dao = OrdersDAO()
        line_info = order_dao.get_order_lines_by_order_id(order_id)

        # verify db response is not empty
        assert line_info, f"Created order line item not found in DB. Order id: {order_id}"

        # get the line items only (exclude shipping)
        line_items = [i for i in line_info if i['order_item_type'] == 'line_item']
        assert len(line_items) == len(exp_products), f"Expected{len(exp_products)} line item but found {len(line_items)}" \
                                                     f" Order id: {order_id}"

        # get list of product ids in the response
        api_product_ids = [i['product_id'] for i in order_json['line_items']]

        for product in exp_products:
            exp_id = product['product_id']
            assert exp_id in api_product_ids, f"Created order does not have at least 1 expected product." \
                                              f"Product id: {product['product_id']}. Order id: {order_id}"
