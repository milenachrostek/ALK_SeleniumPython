from selenium.webdriver.common.by import By


class HomePageLocators():
    """
    Locators used on Home Page
    """
    CONTACT_US_LINK = (By.ID, "contact-link")
    NEWSLETTER = (By.ID, "newsletter-input")
    NEWSLETTER_SUBMIT = (By.NAME, 'submitNewsletter')
    ACCEPT = (By.XPATH, '//*[@id="columns"]/p')
    WOMEN_LINK = (By.XPATH, '//*[@id="block_top_menu"]/ul/li[1]/a')
    T_SHIRTS_LINK = (By.XPATH, '//*[@id="block_top_menu"]/ul/li[3]/a')
    DRESSES_LINK = (By.XPATH, '//*[@id="block_top_menu"]/ul/li[2]/a')
    SEARCH = (By.ID, "search_query_top")
    SEARCH_BTN = (By.NAME, "submit_search")


class CustomerServicePageLocators():
    """
    Locators used on Customer Service Page
    """
    SUBJECT_HEADING = (By.ID, "id_contact")
    CUSTOMER_EMAIL = (By.ID, "email")
    ORDER = (By.ID, "id_order")
    MESSAGE = (By.ID, "message")
    SEND = (By.ID, "submitMessage")
    CONFIRMATION = (By.XPATH, '//*[@id="center_column"]/p')


class WomenPageLocators():
    """
    Locators used on Women Page
    """
    TOPS = (By.ID, "layered_category_4")
    DRESSES = (By.ID, "layered_category_8")
    SIZE_S = (By.ID, "layered_id_attribute_group_1")
    SIZE_M = (By.ID, "layered_id_attribute_group_2")
    SORT_BY = (By.XPATH, '//*[@id="selectProductSort"]')
    COLOR_YELLOW = (By.ID, "layered_id_attribute_group_16")
    COLOR_ORANGE = (By.ID, "layered_id_attribute_group_13")
    RESULT = (By.XPATH, '//*[@id="center_column"]/div[3]/div[2]/div[2]')
    LIST = (By.CLASS_NAME, "icon-th-list")
    PRICE1 = (By.XPATH, '//*[@id="center_column"]/ul/li[1]/div/div/div[3]/div/div[1]/span[1]')
    PRICE2 = (By.XPATH, '//*[@id="center_column"]/ul/li[2]/div/div/div[3]/div/div[1]/span[1]')
    PRICE3 = (By.XPATH, '//*[@id="center_column"]/ul/li[3]/div/div/div[3]/div/div[1]/span')


class ShoppingPageLocators():
    """
    Locators used on Shopping Page
    """
    ADD_CART = (By.XPATH, '//*[@id="center_column"]/ul/li/div/div/div[3]/div/div[2]/a[1]')
    LIST = (By.CLASS_NAME, "icon-th-list")
    ADDED_CART = (By.XPATH, '//*[@id="layer_cart"]/div[1]/div[1]/h2')
    PROCEED = (By.XPATH, '//*[@id="layer_cart"]/div[1]/div[2]/div[4]/a/span')
    SORT_BY = (By.XPATH, '//*[@id="selectProductSort"]')


class SummaryPageLocators():
    """
    Locators used on Summary Page
    """
    ICON_PLUS = (By.XPATH, '//*[@id="cart_quantity_up_1_1_0_0"]/span/i')
    SUMMARY_NUMBER = (By.ID, "summary_products_quantity")
    PROCEED_TO_CHECKOUT = (By.XPATH, '//*[@id="center_column"]/p[2]/a[1]/span')


class CheckoutPageLocators():
    """
    Locators used on Checkout Page
    """
    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "passwd")
    SIGN_IN_BTN = (By.XPATH, '//*[@id="SubmitLogin"]/span')
    ERROR = (By.XPATH, '//div[@class="alert alert-danger"]/ol/li')


class ComparisonPageLocators():
    """
    Locators used on Comparison Page
    """
    LIST = (By.CLASS_NAME, "icon-th-list")
    ADD_COMPARE = (By.XPATH, '//*[@id="center_column"]/ul/li[1]/div/div/div[3]/div/div[3]/div[2]/a')
    ADD_COMPARE2 = (By.XPATH, '//*[@id="center_column"]/ul/li[2]/div/div/div[3]/div/div[3]/div[2]/a')
    COMPARE_BTN = (By.XPATH, '//*[@id="center_column"]/div[3]/div[2]/form')


class ProductComparisonPageLocators():
    """
    Locators used on Product Comparison Page
    """
    PRINTED_DRESS = (By.XPATH, '//*[@id="product_comparison"]/tbody/tr[1]/td[2]/div[3]/span')
    PRINTED_DRESS2 = (By.XPATH, '//*[@id="product_comparison"]/tbody/tr[1]/td[3]/div[3]/span')


class SearchPageLocators():
    """
    Locators used on Search Page
    """
    RESULTS = (By.XPATH, '//*[@id="center_column"]/h1/span[2]')
