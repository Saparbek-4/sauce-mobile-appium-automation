import pytest
import allure
from pages.cart_page import CartPage
from locators.cart_locators import CartLocators

PRODUCT_1 = "Sauce Labs Backpack"
PRODUCT_2 = "Sauce Labs Bike Light"


@allure.feature("Cart")
@allure.story("View cart items")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.functional
@pytest.mark.smoke
def test_cart_view(products_page):

    with allure.step("Add two products to cart"):
        products_page.add_product_to_cart(PRODUCT_1)
        products_page.add_product_to_cart(PRODUCT_2)

    with allure.step("Open cart page"):
        cart = products_page.open_cart()
        assert cart.is_loaded()

    with allure.step("Verify both products are displayed"):
        item_names = cart.get_products()
        assert len(item_names) >= 2
        assert PRODUCT_1 in item_names
        assert PRODUCT_2 in item_names

    with allure.step("Verify cart buttons exist"):
        assert cart.is_visible(CartLocators.REMOVE_BUTTON)
        assert cart.is_visible(CartLocators.CONTINUE_SHOPPING)
        assert cart.is_visible(CartLocators.CHECKOUT_BUTTON)


@allure.feature("Cart")
@allure.story("Remove items from cart")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.functional
def test_cart_remove_item(products_page):

    with allure.step("Add two items to cart"):
        products_page.add_product_to_cart(PRODUCT_1)
        products_page.add_product_to_cart(PRODUCT_2)
        assert products_page.cart_badge_value() == 2

    with allure.step("Open cart"):
        cart = products_page.open_cart()
        assert cart.is_loaded()

    with allure.step("Remove first product"):
        cart.remove_first_product()

    with allure.step("Verify only one product remains"):
        assert products_page.cart_badge_value() == 1
        assert len(cart.get_products()) == 1


@allure.feature("Cart")
@allure.story("Continue shopping from cart")
@allure.severity(allure.severity_level.MINOR)
@pytest.mark.functional
@pytest.mark.smoke
def test_continue_shopping(products_page):

    with allure.step("Add product to cart"):
        products_page.add_product_to_cart(PRODUCT_1)

    with allure.step("Open cart and click Continue Shopping"):
        cart = products_page.open_cart()
        cart.continue_shopping()

    with allure.step("Verify returned to Products page"):
        assert products_page.is_loaded()

    with allure.step("Verify cart badge preserved"):
        assert products_page.cart_badge_value() == 1


@allure.feature("Cart")
@allure.story("Empty cart state")
@allure.severity(allure.severity_level.MINOR)
@pytest.mark.functional
def test_empty_cart(products_page):

    with allure.step("Reset app state to clear cart"):
        menu = products_page.open_menu()
        menu.reset_app_state()
        assert products_page.is_loaded()

    with allure.step("Open cart"):
        cart = products_page.open_cart()
        assert cart.is_loaded()

    with allure.step("Verify cart is empty"):
        assert cart.is_empty()
