
from demostore_automation.src.utilities.genericUtilities import generate_random_string
from demostore_automation.src.api_helpers.ProductsReviewsAPIHelper import ProductsReviewsAPIHelper


class GenericProductsReviewsHelper:

    def __init__(self):
        self.products_reviews_api_helper = ProductsReviewsAPIHelper()

    def create_a_review_for_product(self, product_id, review, reviewer, reviewer_email, rating, expected_status_code=201, **kwargs):

        payload = {
            "product_id": product_id,
            "review": review,
            "reviewer": reviewer,
            "reviewer_email": reviewer_email,
            "rating": rating
        }

        payload.update(kwargs)

        rs_api = self.products_reviews_api_helper.call_create_product_review(
                    payload=payload,
                    expected_status_code=expected_status_code
                )

        return rs_api
