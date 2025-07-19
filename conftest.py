import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import tempfile
import os

@pytest.fixture
def driver():
    options = Options()

    options.add_argument("--start-maximized")
    options.add_argument("--headless=new") 
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")


    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    yield driver

    driver.quit()