from config import BASE_URL
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class AddUserOrder:

    def __init__(self,driver):
        self.driver = driver
        self.base_url = BASE_URL

    def is_user_tag_displayed(self):
        try:
            return self.driver.find_element(By.XPATH, '//h3[text() = "Create User"]').is_displayed()
        except NoSuchElementException:
            return False

    def open_user_order_page(self):
        self.driver.get(self.base_url)
        self.driver.find_element(By.XPATH, "//li[contains(., 'Users')]").click()
    
    def fill_user_form(self, username, order, revenue):
        self.driver.find_element(By.XPATH, '//input[@placeholder="Username"]').send_keys(username)
        self.driver.find_element(By.XPATH, '//input[@placeholder="Orders"]').send_keys(order)
        self.driver.find_element(By.XPATH, '//input[@placeholder="Revenue"]').send_keys(revenue)
        
    def click_save_button(self):
        self.driver.find_element(By.XPATH, '//button[text()="Save"]').click()

    def click_cancel_button(self):
        self.driver.find_element(By.XPATH, '//button[text()="Cancel"]').click()

    def get_alert_text(self, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
            return self.driver.switch_to.alert.text
        except TimeoutException:
            return None

    def accept_alert(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        except TimeoutException:
            return None