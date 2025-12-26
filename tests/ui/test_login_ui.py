import pytest
from pages.login_page import LoginPage

@pytest.mark.ui
def test_user_can_login(driver):
    login_page = LoginPage(driver)
    login_page.open_url("https://automationexercise.com/login")

    login_page.login("testuser@email.com", "password123")

    assert login_page.is_logged_in(), "User failed to log in"
