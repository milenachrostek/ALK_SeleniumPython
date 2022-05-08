from selenium.webdriver.support.select import Select
from pages.base_page import BasePage
from pages.locators import CustomerServicePageLocators


class CustomerServicePage(BasePage):
    """
    Customer Service Page Object
    """

    def choose_subject(self, subject):
        """
        Chooses subject
        """
        el = Select(self.driver.find_element(*CustomerServicePageLocators.SUBJECT_HEADING))
        el.select_by_visible_text(subject)

    def enter_customer_email(self, email):
        """
        Enters customer email
        """
        el = self.driver.find_element(*CustomerServicePageLocators.CUSTOMER_EMAIL)
        el.send_keys(email)

    def enter_order(self, order):
        """
        Enters order ID
        """
        el = self.driver.find_element(*CustomerServicePageLocators.ORDER)
        el.send_keys(order)

    def enter_message(self, message):
        """
        Enters message
        """
        el = self.driver.find_element(*CustomerServicePageLocators.MESSAGE)
        el.send_keys(message)

    def click_send(self):
        """
        Clicks Send button
        """
        el = self.driver.find_element(*CustomerServicePageLocators.SEND)
        el.click()

    def get_confirmation(self):
        """
        Returns confirmation
        """
        el = self.driver.find_element(*CustomerServicePageLocators.CONFIRMATION)
        return el.text



