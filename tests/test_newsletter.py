from tests.base_test import BaseTest


class NewsletterTest(BaseTest):
    """
    Newsletter Test
    """
    def test_newsletter(self):
        """
        TC 004: User is able to send request for a Newsletter
        """
        home_page = self.home_page
        #1. Wpisz email
        home_page.enter_newsletter_email(self.test_data.email)
        #2. Kliknij potwierdzenie
        home_page.click_submit()
        #Oczekiwany rezultat:
        #3. Użytkownik otrzymuje potwierdzenie subskrypcji
        info = "Newsletter : You have successfully subscribed to this newsletter."
        self.assertEqual(home_page.get_newsletter(), info)

