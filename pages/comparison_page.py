from pages.base_page import BasePage
from pages.locators import ComparisonPageLocators
from pages.product_comparison_page import ProductComparisonPage


class ComparisonPage(BasePage):
    """
    Comparison Page Object
    """

    def click_list(self):
        """
        Clicks List View
        """
        el = self.driver.find_element(*ComparisonPageLocators.LIST)
        el.click()

    def click_add_compare(self):
        """
        Clicks Add to Compare
        """
        el = self.driver.find_element(*ComparisonPageLocators.ADD_COMPARE)
        el.click()

    def click_add_compare2(self):
        """
        Clicks Add to Compare
        """
        el = self.driver.find_element(*ComparisonPageLocators.ADD_COMPARE2)
        el.click()

    def click_compare(self):
        """
        Clicks Compare button
        """
        el = self.driver.find_element(*ComparisonPageLocators.COMPARE_BTN)
        el.click()
        return ProductComparisonPage(self.driver)


