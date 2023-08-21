
from demostore_automation.src.utilities.wooAPIUtility import WooAPIUtility
from demostore_automation.src.utilities.genericUtilities import generate_random_email_and_password


class CustomersAPIHelper:

    def __init__(self):
        self.woo_api_utility = WooAPIUtility()

    def call_create_customer(self, email=None, password=None, expected_status_code=201, **kwargs):
        # if email is not provided create one
        if not email:
            rand_info = generate_random_email_and_password()
            email = rand_info['email']

        # if password is not provided create one
        if not password:
            password = 'Password1'

        # create the payload
        payload = dict()
        payload['email'] = email
        payload['password'] = password

        create_user_json = self.woo_api_utility.post('customers', params=payload, expected_status_code=expected_status_code)

        return create_user_json

    def call_delete_customer(self, customer_id):
        return self.woo_api_utility.delete(f'customers/{customer_id}', params={"force": True})