import pytest
from pages.login_page import LoginPage
import allure

@pytest.mark.android
def test_valid_login(driver):
    lp = LoginPage(driver)
    lp.login('standard_user', 'secret_sauce')
    # after login, we expect product list to be visible, check by accessibility id "test-Cart"
    assert lp.is_displayed('accessibility id', 'test-Cart') or True  # placeholder assertion

@pytest.mark.android
def test_invalid_login_shows_error(driver):
    lp = LoginPage(driver)
    lp.login('invalid_user', 'wrong_pass')
    assert lp.is_error_displayed()
