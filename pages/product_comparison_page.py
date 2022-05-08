from pages.base_page import BasePage
from pages.locators import ProductComparisonPageLocators


class ProductComparisonPage(BasePage):
    """
    Product Comparison Page Object
    """
    def get_text(self):
        """
        Returns first compared product
        """
        el = self.driver.find_element(*ProductComparisonPageLocators.PRINTED_DRESS)
        el.location_once_scrolled_into_view
        return el.text

    def get_text2(self):
        """
        Returns second compared product
        """
        el = self.driver.find_element(*ProductComparisonPageLocators.PRINTED_DRESS2)
        return el.text



