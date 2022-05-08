from tests.base_test import BaseTest


class ContactUsTest(BaseTest):
    """
    Contact Us Test
    """
    def test_contact(self):
        """
        TC 006: User is able to contact with customer service
        """
        home_page = self.home_page
        #1. Kliknij Contact Us
        customer_service_page = home_page.click_contact_us()
        #2. Wybierz temat
        customer_service_page.choose_subject(self.test_data.subject)
        #3. Wpisz email
        customer_service_page.enter_customer_email(self.test_data.email)
        #4. Wpisz numer zamówienia
        customer_service_page.enter_order(self.test_data.order)
        #5. Wpisz wiadomość
        customer_service_page.enter_message(self.test_data.message)
        #6. Kliknij Wyślij
        customer_service_page.click_send()
        #Oczekiwany rezultat:
        #7. Użytkownik otrzymuje komunikat „Your message has been successfully sent to our team.”
        statement = "Your message has been successfully sent to our team."
        self.assertEqual(customer_service_page.get_confirmation(), statement)

