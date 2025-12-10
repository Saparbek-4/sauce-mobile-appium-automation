import pytest
import allure
from pages.login_page import LoginPage
from pages.products_page import ProductsPage


# ============================
# LOGIN TEST SUITE
# ============================


@allure.feature("Login")
@allure.story("Successful login")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.functional
def test_login_success_standard_user(driver):
    """
    TC-LG-001 — Успешный вход стандартного пользователя
    """

    login = LoginPage(driver)

    with allure.step("Login using valid credentials"):
        login.login("standard_user", "secret_sauce")

    products_page = ProductsPage(driver)

    with allure.step("Verify that Products page is loaded"):
        assert products_page.is_loaded(), "Products screen must be visible after successful login"

    with allure.step("Verify product list is not empty"):
        assert products_page.product_count() >= 1, "Expected product list after login"

    with allure.step("Verify cart is empty after login"):
        assert products_page.cart_badge_value() == 0


@allure.feature("Login")
@allure.story("Locked out user")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.negative
@pytest.mark.security
def test_login_locked_out_user(driver):
    """
    TC-LG-002 — Вход с locked_out_user (ожидаем ошибку)
    """

    login = LoginPage(driver)

    with allure.step("Attempt login with locked_out_user"):
        login.login("locked_out_user", "secret_sauce")

    with allure.step("Verify error message"):
        error = login.get_error().lower()
        assert "locked out" in error, "Expected locked_out_user error message"


@allure.feature("Login")
@allure.story("Invalid credentials")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.negative
@pytest.mark.security
def test_login_invalid_password(driver):
    """
    TC-LG-003 — Неверный пароль
    """

    login = LoginPage(driver)

    with allure.step("Attempt login with invalid password"):
        login.login("standard_user", "invalid123")

    with allure.step("Verify invalid password error message"):
        error = login.get_error().lower()
        assert "do not match" in error or "not match" in error, \
            "Expected 'password not match' error message"


@allure.feature("Login")
@allure.story("Input validation")
@allure.severity(allure.severity_level.MINOR)
@pytest.mark.validation
def test_login_empty_username(driver):
    """
    TC-LG-004 — Пустое имя пользователя (валидация)
    """

    login = LoginPage(driver)

    with allure.step("Submit login form with empty username"):
        login.enter_username("")
        login.enter_password("secret_sauce")
        login.tap_login()

    with allure.step("Verify validation error"):
        error = login.get_error().lower()
        assert "username is required" in error, "Expected validation error for empty username"
