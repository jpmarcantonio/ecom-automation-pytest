import pytest
import logging as logger
from demostore_automation.src.dao.products_dao import ProductsDAO
from demostore_automation.src.generic_helpers.generic_order_helpers import GenericOrderHelper

pytestmark = [pytest.mark.beregression, pytest.mark.besmoke, pytest.mark.orders_api]

@pytest.mark.smoke
@pytest.mark.orders
@pytest.mark.tcid48
def test_create_paid_order_guest_user():
    """
    Test function to verify the creation of a paid order using a guest user.

    This test function performs the following steps:
    1. Retrieves a random product from the database.
    2. Calls the 'create_order' method from the GenericOrderHelper class to create an order with the retrieved product.
    3. Verifies the created order by checking the order details in the database.

    :return: None
    """

    logger.info("Testing 'Create Order' using guest user...")

    # need product for the order
    product_dao = ProductsDAO()
    rand_product = product_dao.get_random_product_from_db()
    product_id = rand_product[0]['ID']

    # make the call to create order
    generic_order_helper = GenericOrderHelper()
    args = {"line_items": [
                {
                    "product_id": product_id,
                    "quantity": 2
                }]
            }

    api_order_info = generic_order_helper.create_order(additional_args=args)

    # verify the order is created by checking the database
    expected_cust_id = 0  # because we are using guest user
    expected_products = [{'product_id': product_id}]
    generic_order_helper.verify_order_is_created(api_order_info, expected_cust_id, expected_products)

    # verify the order is created by calling API