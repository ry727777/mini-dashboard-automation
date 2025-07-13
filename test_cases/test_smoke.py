from action.dashboard_page import DashboardPage

def test_smoke_title(driver):
    dashboard = DashboardPage(driver)
    dashboard.open()
    title = dashboard.is_title_correct
    assert title, f"Title is not correct, current title is {title}"