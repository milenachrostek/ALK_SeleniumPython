import time

from tests.base_test import BaseTest


class ShoppingTest(BaseTest):
    """
    Shopping Test
    """
    def test_shopping(self):
        """
        TC 001: User does not fill the email field while shopping
        """
        home_page = self.home_page
        #1. Kliknij T-Shirt
        shopping_page = home_page.click_tshirt_link()
        #2. Wybierz wszystkie produkty dostęþne w magazynie
        shopping_page.choose_sort_by(self.test_data.sort_by2)
        #3. Kliknij widok listy
        shopping_page.click_list()
        #4. Kliknij dodaj do koszyka
        shopping_page.click_add_cart()
        time.sleep(10)
        #5. Wyświetlenie komunikatu o pozytywnym dodaniu produktu do koszyka
        added = "Product successfully added to your shopping cart"
        self.assertEqual(shopping_page.get_added(), added)
        #6. Kliknij przejdź do kasy
        summary_page = shopping_page.click_proceed()
        #7. Zwiększ liczbę produktów w koszyku
        summary_page.click_icon_plus()
        time.sleep(10)
        #8. Wyświetlenie oczekiwanej liczby produktów w koszyku
        summary = "2 Products"
        self.assertEqual(summary_page.get_summary_number(), summary)
        #9. Kliknij przejdź do kasy
        checkout_page = summary_page.click_proceed_to_checkout()
        #10. Wpisz hasło
        checkout_page.enter_password(self.test_data.password)
        #11. Kliknij Sign In
        checkout_page.click_sign_in_checkout()
        #Oczekiwany rezultat:
        #12. Użytkownik otrzymuje komunikat "An email address required"
        error = ["An email address required."]
        self.assertCountEqual(checkout_page.get_error_messages(), error)
