from tests.base_test import BaseTest


class SearchTest(BaseTest):
    """
    Search Test
    """
    def test_search(self):
        """
        TC 003: User is able to search for products
        """
        home_page = self.home_page
        #1. Wpisz szukany produkt
        home_page.enter_search(self.test_data.search)
        #2. Kliknij Szukaj
        search_page = home_page.click_search()
        #Oczekiwany rezultat:
        #3. Użytkownik otrzymuje liczbę zwróconych rezultatów
        results = '1 result has been found.'
        self.assertEqual(search_page.get_search_result(), results)

