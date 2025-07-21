from action.AddUserOrder import AddUserOrder
import pytest
import random
import allure


@pytest.mark.regression
@allure.feature("Add User Order")
@allure.story("Add User Order Tests")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Test Add User Order Functionality")
def test_add_user_order(driver):
    page = AddUserOrder(driver)

    with allure.step("Open User Order Page"):
        page.open_user_order_page()
        assert page.is_user_tag_displayed(), "User tag is not displayed on the page"

    with allure.step("Fill User Form"):
        # Fill the user form with random data
        username = f"testuser{random.randint(100, 900)}"
        order = random.randint(100, 999)
        revenue = random.randint(11111, 99999)
    page.fill_user_form(username, order, revenue)

    with allure.step("Click Save Button and check alert for User create!"):
        page.click_save_button()
        alert_text = page.get_alert_text()
        assert "User created!" in alert_text, f"Expected success message not found: {alert_text}"
        page.accept_alert()
