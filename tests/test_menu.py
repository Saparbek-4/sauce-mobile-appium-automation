import pytest
import allure
from pages.login_page import LoginPage


@allure.feature("Menu")
@allure.story("Open and close menu")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.smoke
@pytest.mark.functional
def test_menu_open_and_close(products_page):
    """TC-MN-001 — Open and close menu"""

    with allure.step("Open menu"):
        menu = products_page.open_menu()
        assert menu.is_loaded(), "Menu should be visible after opening"

    with allure.step("Close menu"):
        menu.close_menu()
        assert menu.is_closed(), "Menu should close correctly"


@allure.feature("Menu")
@allure.story("User logout")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.security
def test_logout(driver, products_page):
    """TC-MN-002 — Logout"""

    with allure.step("Open menu"):
        menu = products_page.open_menu()
        assert menu.is_loaded(), "Menu should be visible"

    with allure.step("Tap logout"):
        menu.logout()

    with allure.step("Verify redirected to Login screen"):
        login_page = LoginPage(driver)
        assert login_page.is_login_screen(), "Should return to login screen after logout"


@allure.feature("Menu")
@allure.story("Reset application state")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.functional
def test_reset_app_state(products_page):
    """TC-MN-003 — Reset App State"""

    with allure.step("Add product into cart"):
        products_page.add_product_to_cart("Sauce Labs Backpack")
        assert products_page.cart_badge_value() == 1

    with allure.step("Open menu"):
        menu = products_page.open_menu()
        assert menu.is_loaded(), "Menu should be visible"

    with allure.step("Reset app state"):
        menu.reset_app_state()

    with allure.step("Verify cart was cleared"):
        assert products_page.cart_badge_value() == 0, \
            "After Reset App State the badge should be 0"
