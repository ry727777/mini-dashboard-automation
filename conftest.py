import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    # Optional: Headless mode for CI
    # options.add_argument("--headless")

    # Use ChromeDriverManager to auto-download driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    yield driver  # This provides the driver to test functions

    driver.quit()  # Clean up after test
