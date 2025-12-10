import pytest
import allure
from pages.checkout_info_page import CheckoutInfoPage

PRODUCT = "Sauce Labs Backpack"


# ====================== E2E FLOW ======================

@allure.feature("Checkout")
@allure.story("Full purchase flow")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.e2e
def test_full_checkout(products_page, driver):

    with allure.step("Add product to cart"):
        products_page.add_product_to_cart(PRODUCT)
        assert products_page.cart_badge_value() == 1

    with allure.step("Open cart and go to checkout"):
        cart = products_page.open_cart()
        cart.go_to_checkout()

    with allure.step("Fill checkout info"):
        info = CheckoutInfoPage(driver)
        assert info.is_loaded()
        info.fill_form("John", "Doe", "12345")
        overview = info.submit()

    with allure.step("Verify Overview screen"):
        assert overview.is_loaded()

    with allure.step("Finish checkout"):
        complete = overview.finish()
        assert complete.is_loaded()

    with allure.step("Verify cart badge reset to 0"):
        assert products_page.cart_badge_value() == 0



# ====================== VALIDATION TESTS ======================

@allure.feature("Checkout")
@allure.story("Input validation")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.validation
def test_empty_first_name(driver, products_page):

    with allure.step("Open checkout page"):
        products_page.add_product_to_cart(PRODUCT)
        cart = products_page.open_cart()
        cart.go_to_checkout()

    info = CheckoutInfoPage(driver)
    assert info.is_loaded()

    with allure.step("Leave first name empty and submit"):
        info.fill_form("", "Doe", "12345")
        info.submit()

    with allure.step("Verify validation message"):
        assert "First Name is required" in info.get_error()


@allure.feature("Checkout")
@allure.story("Input validation")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.validation
def test_empty_zip(products_page):

    with allure.step("Open checkout page"):
        products_page.add_product_to_cart(PRODUCT)
        cart = products_page.open_cart()
        cart.go_to_checkout()

    info = CheckoutInfoPage(products_page.driver)

    with allure.step("Leave ZIP empty and submit"):
        info.fill_form("John", "Doe", "")
        info.submit()

    with allure.step("Verify validation message"):
        assert "Postal Code is required" in info.get_error()



# ====================== FUNCTIONAL TESTS ======================

@allure.feature("Checkout")
@allure.story("Cancel checkout")
@pytest.mark.functional
def test_checkout_cancel(products_page):

    with allure.step("Open checkout page"):
        products_page.add_product_to_cart(PRODUCT)
        cart = products_page.open_cart()
        cart.go_to_checkout()

    info = CheckoutInfoPage(products_page.driver)

    with allure.step("Submit form with valid data"):
        overview = info.submit()

    with allure.step("Cancel on overview screen"):
        overview.cancel()

    with allure.step("Verify returned to Products page"):
        assert products_page.is_loaded()



# ====================== SMOKE + FUNCTIONAL ======================

@allure.feature("Checkout")
@allure.story("Verify totals calculation")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.functional
@pytest.mark.smoke
def test_overview_totals(products_page):

    with allure.step("Open checkout page"):
        products_page.add_product_to_cart(PRODUCT)
        cart = products_page.open_cart()
        cart.go_to_checkout()

    info = CheckoutInfoPage(products_page.driver)
    assert info.is_loaded()

    with allure.step("Fill checkout form"):
        info.fill_form("John", "Doe", "12345")
        overview = info.submit()

    with allure.step("Verify overview screen loads"):
        assert overview.is_loaded()

    with allure.step("Read totals and verify calculation"):
        totals = overview.get_totals()

        item_total = parse_price(totals["item_total"])
        tax = parse_price(totals["tax"])
        total = parse_price(totals["total"])

        assert total == round(item_total + tax, 2), "Total must equal Item Total + Tax"


def parse_price(text: str) -> float:
    return float(text.split("$")[1])
