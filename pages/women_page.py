from selenium.webdriver.support.select import Select
from pages.base_page import BasePage
from pages.locators import WomenPageLocators


class WomenPage(BasePage):
    """
    Women Page Object
    """

    def choose_category(self, catalog):
        """
        Chooses Category
        """
        if catalog == "Tops":
            # Choose Tops
            self.driver.find_element(*WomenPageLocators.TOPS).click()
        else:
            # Choose Dresses
            self.driver.find_element(*WomenPageLocators.DRESSES).click()

    def choose_size(self, size):
        """
        Chooses Size
        """
        if size == "M":
            # Choose Tops
            self.driver.find_element(*WomenPageLocators.SIZE_M).click()
        else:
            # Choose Dresses
            self.driver.find_element(*WomenPageLocators.SIZE_S).click()

    def choose_color(self, color):
        """
        Chooses color
        """
        if color == "Yellow":
            self.driver.find_element(*WomenPageLocators.COLOR_YELLOW).click()
        else:
            self.driver.find_element(*WomenPageLocators.COLOR_ORANGE).click()

    def choose_sort_by(self, sort_by):
        """
        Chooses Sort By
        """
        el = Select(self.driver.find_element(*WomenPageLocators.SORT_BY))
        el.select_by_visible_text(sort_by)

    def click_list(self):
        """
        CLicks List View
        """
        self.driver.find_element(*WomenPageLocators.LIST).click()

    def get_results(self):
        """
        Returns displayed result
        """
        el = self.driver.find_element(*WomenPageLocators.RESULT)
        return el.text

    def get_price1(self):
        """
        Returns Price of first displayed product
        """
        el = self.driver.find_element(*WomenPageLocators.PRICE1)
        return el.text

    def get_price2(self):
        """
        Returns Price of second displayed product
        """
        el = self.driver.find_element(*WomenPageLocators.PRICE2)
        return el.text

    def get_price3(self):
        """
        Returns Price of third displayed product
        """
        el = self.driver.find_element(*WomenPageLocators.PRICE3)
        return el.text
