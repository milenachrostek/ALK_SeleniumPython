from pages.base_page import BasePage
from pages.checkout_page import CheckoutPage
from pages.locators import SummaryPageLocators


class SummaryPage(BasePage):
    """
    Summary Page Object
    """

    def click_icon_plus(self):
        """
        Clicks Icon Plus
        """
        self.driver.find_element(*SummaryPageLocators.ICON_PLUS).click()

    def get_summary_number(self):
        """
        Returns number of added products
        """
        el = self.driver.find_element(*SummaryPageLocators.SUMMARY_NUMBER)
        return el.text

    def click_proceed_to_checkout(self):
        """
        Clicks Proceed to Checkout button and returns Checkout Page
        """
        self.driver.find_element(*SummaryPageLocators.PROCEED_TO_CHECKOUT).click()
        return CheckoutPage(self.driver)
