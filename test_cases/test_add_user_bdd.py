from action.AddUserOrder import AddUserOrder
import pytest
import random
from pytest_bdd import given, when, then, scenarios, parsers

scenarios('../features/add_user.feature')

# Fixture that initializes the POM using the WebDriver
@pytest.fixture
def page(driver):  
    return AddUserOrder(driver)

@given('the user is on the "Add User Page"')
def open_user_order_page(page):
    page.open_user_order_page()
    assert page.is_user_tag_displayed(), "User tag is not displayed on the page"

@when(parsers.parse('the user enters "{username}" as username, "{order}" as order, and "{revenue}" as revenue'))
def fill_user_form(page, username, order, revenue):
    page.fill_user_form(username, order, revenue)

@when('click on Submit button')
def click_save_button(page):
    page.click_save_button()

@then('user should see the alert "User created!"')
def check_alert(page):
    assert page.get_alert_text() == "User created!", "Success alert is not displayed"
    page.accept_alert()
