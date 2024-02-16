
import pytest
import logging as logger
import random
from demostore_automation.src.generic_helpers.generic_products_helper import GenericProductsHelper
from demostore_automation.src.generic_helpers.generic_products_reviews_helper import GenericProductsReviewsHelper
from demostore_automation.src.utilities.genericUtilities import generate_random_string
from demostore_automation.src.utilities.genericUtilities import generate_random_email_and_password

class TestProductReviewsSmoke(object):

    @pytest.mark.edb13
    def test_verify_create_product_review_endpoint_creates_review(self):
        """

        :return:
        """
        logger.info("test_verify_create_product_review_endpoint_creates_review")

        # create a review

        ## create a product for the test
        product_helper = GenericProductsHelper()
        product_info = product_helper.create_a_product()
        product_id = product_info['id']


        ## create a review
        product_review_helper = GenericProductsReviewsHelper()
        qty_review_to_add = 5

        for i in range(qty_review_to_add):
            # product_id, review, reviewer, reviewer_email, rating, expected_status_code=201
            review = generate_random_string(30)
            reviewer_name = generate_random_string(15)
            reviewer_email = generate_random_email_and_password()['email']
            rating = random.randint(0, 5)
            rs_review_api = product_review_helper.create_a_review_for_product(
                    product_id,
                    review,
                    reviewer_name,
                    reviewer_email,
                    rating
                )

            #verify the response
            assert rs_review_api['product_id'] == product_id, f"Create feview response unexpected 'product_id'. Expected: {product_id}, Actual: {rs_review_api['product_id']}"
            assert rs_review_api['review'] == review, f"Create review response unexpected 'review'. Expected: {review}, Actual: {rs_review_api['review']}"
            assert rs_review_api['rating'] == rating, f"Create review response unexpected 'rating'. Expected: {rating}, Actual: {rs_review_api['rating']}"
            assert rs_review_api['reviewer'] == reviewer_name, f"Create review response unexpected 'reviewer_name'. Expected: {reviewer_name}, Actual: {rs_review_api[reviewer_name]}"
            assert rs_review_api['reviewer_email'] == reviewer_email, f"Create review response unexpected 'reviewer_email'. Expected: {reviewer_email}, Actual: {rs_review_api[reviewer_email]}"
            assert rs_review_api['status'] == 'approved', f"Create review response unexpected 'status'. Expected: 'approved', Actual: {rs_review_api['status']}"
        breakpoint()

        # verify review is created

        ## get all reviews for the given product

        ## verify the review created is attached to the product