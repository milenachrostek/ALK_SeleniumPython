from faker import Faker


class TestData:
    def __init__(self):
        fake = Faker()
        self.email = fake.email()
        self.password = "password123"
        self.subject = "Customer service"
        self.order = "ID1234"
        self.message = 'Hi AutomationPractice'
        self.sort_by = 'Price: Lowest first'
        self.catalog = "Dresses"
        self.size = "M"
        self.color = "Yellow"
        self.sort_by2 = 'In stock'
        self.search = 'Blouses'
