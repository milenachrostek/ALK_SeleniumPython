from pages.base_page import BasePage
from pages.locators import CheckoutPageLocators


class CheckoutPage(BasePage):
    """
    Checkout Page Object
    """

    def enter_email(self, email):
        pass

    def enter_password(self, password):
        """
        Enters password
        """
        password_input = self.driver.find_element(*CheckoutPageLocators.PASSWORD)
        password_input.click()
        password_input.send_keys(password)

    def click_sign_in_checkout(self):
        """
        Clicks Sign In button
        """
        el = self.driver.find_element(*CheckoutPageLocators.SIGN_IN_BTN)
        el.click()

    def get_error_messages(self):
        """
        Returns error message
        """
        error = self.driver.find_elements(*CheckoutPageLocators.ERROR)
        error_texts = []
        for e in error:
            error_texts.append(e.text)
        return error_texts

