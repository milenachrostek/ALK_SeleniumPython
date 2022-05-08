from pages.base_page import BasePage
from pages.locators import SearchPageLocators


class SearchPage(BasePage):
    """
    Search Page Object
    """
    def get_search_result(self):
        """
        Returns searched results
        """
        el = self.driver.find_element(*SearchPageLocators.RESULTS)
        return el.text



