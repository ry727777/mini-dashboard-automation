from .generic_function import GenericFunction

class DashboardPage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = GenericFunction().get_base_url()

    def open(self):
        self.driver.get(self.base_url)

    def is_title_correct(self):
        print(self.driver.title)
        return "React App" in self.driver.title