import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage


# ============================
# LOGIN TEST SUITE
# ============================


@pytest.mark.smoke
@pytest.mark.functional
def test_login_success_standard_user(driver):
    """
    TC-LG-001 — Успешный вход стандартного пользователя
    """
    login = LoginPage(driver)
    products_page = ProductsPage(driver)

    # Act
    login.login("standard_user", "secret_sauce")

    # Assert
    assert products_page.is_loaded(), "Products screen must be visible after successful login"
    assert products_page.product_count() >= 1, "Expected at least 6 products after login"
    assert products_page.cart_badge_value() == 0, "Cart should be empty after login"


@pytest.mark.negative
@pytest.mark.security
def test_login_locked_out_user(driver):
    """
    TC-LG-002 — Вход с locked_out_user (ожидаем ошибку)
    """
    login = LoginPage(driver)

    # Act
    login.login("locked_out_user", "secret_sauce")

    # Assert
    error = login.get_error().lower()
    assert "locked out" in error, "Expected locked_out_user error message"


@pytest.mark.negative
@pytest.mark.security
def test_login_invalid_password(driver):
    """
    TC-LG-003 — Неверный пароль
    """
    login = LoginPage(driver)

    # Act
    login.login("standard_user", "invalid123")

    # Assert
    error = login.get_error().lower()
    assert "do not match" in error, "Expected 'password not match' error message"


@pytest.mark.validation
def test_login_empty_username(driver):
    """
    TC-LG-004 — Пустое имя пользователя (валидация)
    """
    login = LoginPage(driver)

    # Act
    login.enter_username("")  # intentionally empty
    login.enter_password("secret_sauce")
    login.tap_login()

    # Assert
    error = login.get_error().lower()
    assert "username is required" in error, "Expected validation error for empty username"
