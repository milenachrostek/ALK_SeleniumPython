from pages.base_page import BasePage
from pages.comparison_page import ComparisonPage
from pages.customer_service_page import CustomerServicePage
from pages.locators import HomePageLocators
from pages.search_page import SearchPage
from pages.shopping_page import ShoppingPage
from pages.women_page import WomenPage


class HomePage(BasePage):
    """
    Home Page Object
    """

    def click_dresses(self):
        """
        Clicks Dresses Link and returns Comparison Page
        """
        el = self.driver.find_element(*HomePageLocators.DRESSES_LINK)
        el.click()
        return ComparisonPage(self.driver)

    def click_contact_us(self):
        """
        Clicks Contact Us link and returns Customer Service instance
        """
        el = self.driver.find_element(*HomePageLocators.CONTACT_US_LINK)
        el.click()
        return CustomerServicePage(self.driver)

    def enter_search(self, search):
        """
        Enters search word
        """
        el = self.driver.find_element(*HomePageLocators.SEARCH)
        el.send_keys(search)

    def click_search(self):
        """
        Clicks Search button and returns Search Page
        """
        el = self.driver.find_element(*HomePageLocators.SEARCH_BTN)
        el.click()
        return SearchPage(self.driver)

    def enter_newsletter_email(self, email):
        """
        Enters email
        """
        el = self.driver.find_element(*HomePageLocators.NEWSLETTER)
        el.send_keys(email)

    def click_submit(self):
        """
        Clicks newsletter submit button
        """
        el = self.driver.find_element(*HomePageLocators.NEWSLETTER_SUBMIT)
        el.click()

    def get_newsletter(self):
        """
        Returns confirmation of acceptance
        """
        el = self.driver.find_element(*HomePageLocators.ACCEPT)
        return el.text

    def click_tshirt_link(self):
        """
        Clicks T-shirts Link and returns Shopping Page
        """
        el = self.driver.find_element(*HomePageLocators.T_SHIRTS_LINK)
        el.click()
        return ShoppingPage(self.driver)

    def click_women(self):
        """
        Clicks Women Link and returns Women Page
        """
        el = self.driver.find_element(*HomePageLocators.WOMEN_LINK)
        el.click()
        return WomenPage(self.driver)

    def _verify_page(self):
        """
        Verifies Home Page
        """
        pass