from selenium.webdriver.support.select import Select
from pages.base_page import BasePage
from pages.locators import ShoppingPageLocators
from pages.summary_page import SummaryPage


class ShoppingPage(BasePage):
    """
    Shopping Page Object
    """
    def click_list(self):
        """
        CLicks List View
        """
        self.driver.find_element(*ShoppingPageLocators.LIST).click()

    def choose_sort_by(self, sort_by2):
        """
        Chooses Sort By
        """
        el = Select(self.driver.find_element(*ShoppingPageLocators.SORT_BY))
        el.select_by_visible_text(sort_by2)

    def click_add_cart(self):
        """
        Clicks Add to Cart button
        """
        el = self.driver.find_element(*ShoppingPageLocators.ADD_CART)
        el.location_once_scrolled_into_view
        el.click()

    def get_added(self):
        """
        Returns confirmation text
        """
        el = self.driver.find_element(*ShoppingPageLocators.ADDED_CART)
        return el.text

    def click_proceed(self):
        """
        Clicks Proceed To Checkout button and returns Summary Page
        """
        el = self.driver.find_element(*ShoppingPageLocators.PROCEED)
        el.click()
        return SummaryPage(self.driver)



