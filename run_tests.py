import unittest

from tests.test_shopping import ShoppingTest
from tests.women_test import WomenTest
from tests.search_test import SearchTest
from tests.test_newsletter import NewsletterTest
from tests.comparison_test import ComparisonTest
from tests.contact_test import ContactUsTest

test_shopping = unittest.TestLoader().loadTestsFromTestCase(ShoppingTest)
women_test = unittest.TestLoader().loadTestsFromTestCase(WomenTest)
search_test = unittest.TestLoader().loadTestsFromTestCase(SearchTest)
test_newsletter = unittest.TestLoader().loadTestsFromTestCase(NewsletterTest)
comparison_test = unittest.TestLoader().loadTestsFromTestCase(ComparisonTest)
contact_test = unittest.TestLoader().loadTestsFromTestCase(ContactUsTest)

tests_for_run = [
    # TC 1.
    test_shopping,
    # TC 2.
    women_test,
    # TC 3.
    search_test,
    # TC 4.
    test_newsletter,
    # TC 5.
    comparison_test,
    # TC 6.
    contact_test
]

test_suite = unittest.TestSuite(tests_for_run)
