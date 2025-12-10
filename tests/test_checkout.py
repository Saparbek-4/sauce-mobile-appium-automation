import pytest
from pages.checkout_info_page import CheckoutInfoPage


PRODUCT = "Sauce Labs Backpack"


@pytest.mark.e2e
def test_full_checkout(products_page, driver):
    # Add product
    products_page.add_product_to_cart(PRODUCT)
    assert products_page.cart_badge_value() == 1

    # Open cart
    cart = products_page.open_cart()
    cart.go_to_checkout()

    # Step 1 → Info page
    info = CheckoutInfoPage(driver)
    assert info.is_loaded()

    info.fill_form("John", "Doe", "12345")
    overview = info.submit()

    # Step 2 → Overview
    assert overview.is_loaded()

    complete = overview.finish()

    # Step 3 → Complete
    assert complete.is_loaded()

    # Badge should reset
    assert products_page.cart_badge_value() == 0
    
    
@pytest.mark.validation
def test_empty_first_name(driver, products_page):
    products_page.add_product_to_cart(PRODUCT)
    cart = products_page.open_cart()
    cart.go_to_checkout()

    info = CheckoutInfoPage(driver)
    assert info.is_loaded()

    info.fill_form("", "Doe", "12345")
    info.submit()

    assert "First Name is required" in info.get_error()


@pytest.mark.validation
def test_empty_zip(products_page):
    products_page.add_product_to_cart(PRODUCT)
    cart = products_page.open_cart()
    cart.go_to_checkout()

    info = CheckoutInfoPage(products_page.driver)

    info.fill_form("John", "Doe", "")
    info.submit()

    assert "Postal Code is required" in info.get_error()
    
@pytest.mark.functional
def test_checkout_cancel(products_page):
    products_page.add_product_to_cart(PRODUCT)
    cart = products_page.open_cart()
    cart.go_to_checkout()

    info = CheckoutInfoPage(products_page.driver)

    overview = info.submit()  # valid form
    overview.cancel()

    # Should return to products page
    assert products_page.is_loaded()

@pytest.mark.functional
def test_overview_totals(products_page):
    products_page.add_product_to_cart(PRODUCT)
    cart = products_page.open_cart()
    cart.go_to_checkout()

    info = CheckoutInfoPage(products_page.driver)
    assert info.is_loaded()

    info.fill_form("John", "Doe", "12345")
    overview = info.submit()

    # Step 2 → Overview
    assert overview.is_loaded()

    totals = overview.get_totals()
    
    item_total = parse_price(totals["item_total"])
    tax = parse_price(totals["tax"])
    total = parse_price(totals["total"])

    assert total == round(item_total + tax, 2)
    
    
    
def parse_price(text: str) -> float:
    return float(text.split("$")[1])