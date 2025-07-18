from config import BASE_URL
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class DashBoardPage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = BASE_URL

    def open_dashboard_page(self):
        self.driver.get(self.base_url)

    def is_header_displayed(self):
        try:
            return self.driver.find_element(By.XPATH, '//h2[text() = "My Dashboard"]').is_displayed() 
        except NoSuchElementException:
            return False

    def is_search_bar_displayed(self):
        try:
            return self.driver.find_element(By.XPATH, '//input[@placeholder="Search by username..."]').is_displayed()
        except NoSuchElementException:
            return False

    def is_table_displayed(self):
        try:
            return self.driver.find_element(By.CLASS_NAME, 'dashboard-table').is_displayed()
        except NoSuchElementException:
            return False

    def is_table_columns_displayed(self):
        expected_headers = ["Users", "Total Orders", "Total Revenue"]
        actual_headers = [el.text for el in self.driver.find_elements(By.XPATH, '//table//th')]
        return all(header in actual_headers for header in expected_headers)