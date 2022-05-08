import time
from tests.base_test import BaseTest


class ComparisonTest(BaseTest):
    """
    Comparison Test
    """
    def test_compare(self):
        """
        TC 005: User is able to compare products
        """
        home_page = self.home_page
        #1. Kliknij Dresses
        comparison_page = home_page.click_dresses()
        #2. Kliknij List View
        comparison_page.click_list()
        #3. Kliknij Add to Compare
        comparison_page.click_add_compare()
        time.sleep(10)
        #4. Kliknij Add to Compare
        comparison_page.click_add_compare2()
        time.sleep(10)
        #5. Kliknij Compare
        product_comparison_page = comparison_page.click_compare()
        time.sleep(5)
        #Oczekiwany rezultat:
        #6. Użytkownik otrzymuje porównanie cen dwóch sukienek Printed Dress
        price = "$26.00"
        self.assertEqual(product_comparison_page.get_text(), price)
        price2 = "$50.99"
        self.assertEqual(product_comparison_page.get_text2(), price2)
