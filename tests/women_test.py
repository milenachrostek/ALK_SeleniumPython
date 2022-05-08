import time
from tests.base_test import BaseTest


class WomenTest(BaseTest):
    """
    Sort By Test
    """
    def test_sort(self):
        """
        TC 002: User is able to sort products
        """
        home_page = self.home_page
        #1. Kliknij Women
        women_page = home_page.click_women()
        #2. Wybierz kategorię Dresses
        women_page.choose_category(self.test_data.catalog)
        #3. Wybierz rozmiar M
        women_page.choose_size(self.test_data.size)
        #4. Wybierz kolor Yellow
        women_page.choose_color(self.test_data.color)
        #5. Wybierz sortowanie od najniższej ceny
        women_page.choose_sort_by(self.test_data.sort_by)
        #6. Kliknij widok listy
        women_page.click_list()
        time.sleep(10)
        #7. Wyświetlenie oczekiwanej liczby przefiltrowanych produktów
        result = "Showing 1 - 3 of 3 items"
        self.assertEqual(women_page.get_results(), result)
        #Oczekiwany rezultat:
        #8. Użytkownik otrzymuje listę przefiltrowanych produktów od najtańszego do najdroższego
        price1 = "$16.40"
        self.assertEqual(women_page.get_price1(), price1)
        price2 = "$28.98"
        self.assertEqual(women_page.get_price2(), price2)
        price3 = "$30.50"
        self.assertEqual(women_page.get_price3(), price3)
