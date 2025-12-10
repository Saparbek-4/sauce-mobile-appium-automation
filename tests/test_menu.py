import pytest
from pages.login_page import LoginPage
from pages.menu_page import MenuPage


# @pytest.mark.functional
# def test_menu_open_and_close(products_page):
#     """TC-MN-001 — Открытие и закрытие меню"""
#     menu = products_page.open_menu()
    
#     assert menu.is_loaded(), "Меню не полностью загружена"
    
#     # Закрываем
#     menu.close_menu()

#     assert menu.is_closed(), "Меню должно закрываться корректно"

# @pytest.mark.functional
# @pytest.mark.security
# def test_logout(driver, products_page):
#     """TC-MN-002 — Logout"""
#     menu = products_page.open_menu()
    
#     assert menu.is_loaded(), "Меню не полностью загружена"
#     menu.logout()
    
#     login_page = LoginPage(driver)
    
#     assert login_page.is_login_screen(), "После Logout должен быть экран логина"

@pytest.mark.functional
def test_reset_app_state(products_page):
    """TC-MN-003 — Reset App State"""
    # Добавляем товар для проверки сброса
    products_page.add_product_to_cart("Sauce Labs Backpack")
    assert products_page.cart_badge_value() == 1

    # Сбрасываем состояние приложения
    menu = products_page.open_menu()
    assert menu.is_loaded(), "Меню не полностью загружена"
    
    menu.reset_app_state()

    # Проверяем, что сброс удался
    assert products_page.cart_badge_value() == 0, "После Reset App State badge должен быть 0"