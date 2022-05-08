from pages.home_page import HomePage
from tests.test_data import TestData
from selenium import webdriver
import unittest


class BaseTest(unittest.TestCase):
    """
    Base class for each test
    """
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("https://automationpractice.com/")
        self.driver.implicitly_wait(10)
        self.home_page = HomePage(self.driver)
        self.test_data = TestData()

    def tearDown(self):
        self.driver.quit()
