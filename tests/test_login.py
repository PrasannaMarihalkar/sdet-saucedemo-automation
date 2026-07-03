import pytest

from pages.login_page import LoginPage

def test_successful_login(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")
    assert "inventory.html" in driver.current_url

def test_login_with_wrong_password(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "wrong_password")
    error = login_page.get_error_message()
    assert "do not match" in error.lower()

def test_locked_out_user(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("locked_out_user", "secret_sauce")
    error = login_page.get_error_message()
    assert "locked out" in error.lower()

def test_empty_credentials(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("", "")
    error = login_page.get_error_message()
    assert "username is required" in error.lower()

@pytest.mark.parametrize("username,password,expected_error", [
    ("", "secret_sauce", "username is required"),
    ("standard_user", "", "password is required"),
    ("invalid_user", "secret_sauce", "do not match"),
])
def test_login_validation(driver, username, password, expected_error):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login(username, password)
    error = login_page.get_error_message().lower()
    assert expected_error in error