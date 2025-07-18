from action.DashboardPage import DashBoardPage
import pytest
import allure

@pytest.mark.regression
@allure.feature("Dashboard Page")
@allure.story("Dashboard Page Tests")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Test Dashboard Page Elements")
def test_dashboard_page(driver):
    page = DashBoardPage(driver)

    
    page.open_dashboard_page()

    with allure.step("Verify Dashboard Header"):
        assert page.is_header_displayed(), "Dashboard header is not displayed"

    with allure.step("Verify Search Bar"):
        assert page.is_search_bar_displayed(), "Search bar is not displayed"

    with allure.step("Verify Table"):
        assert page.is_table_displayed(), "Table is not displayed"

    with allure.step("Verify Table Columns"):
        assert page.is_table_columns_displayed(), "Table columns are not displayed"