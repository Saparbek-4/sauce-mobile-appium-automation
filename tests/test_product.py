import pytest

@pytest.mark.smoke
@pytest.mark.functional
def test_products_screen_elements(products_page):
    assert products_page.product_count() >= 1
    names = products_page.get_all_product_names()
    assert len(names) >= 1


@pytest.mark.functional
def test_add_item_to_cart(products_page):
    products_page.add_product_to_cart("Sauce Labs Bike Light")
    assert products_page.cart_badge_value() == 1


@pytest.mark.functional
def test_remove_from_products(products_page):
    products_page.add_product_to_cart("Sauce Labs Bike Light")
    assert products_page.cart_badge_value() == 1

    products_page.remove_product_from_cart("Sauce Labs Bike Light")
    assert products_page.cart_badge_value() == 0


@pytest.mark.functional
def test_add_two_items(products_page):
    products_page.add_product_to_cart("Sauce Labs Backpack")
    products_page.add_product_to_cart("Sauce Labs Bike Light")
    assert products_page.cart_badge_value() == 2


@pytest.mark.functional
@pytest.mark.parametrize(
    "sort_method, reverse, description",
    [
        ("sort_by_az", False, "Sort A → Z"),
        ("sort_by_za", True, "Sort Z → A"),
        ("sort_by_low_high", False, "Price Low → High"),
        ("sort_by_high_low", True, "Price High → Low"),
    ]
)
def test_sorting(products_page, sort_method, reverse, description):

    getattr(products_page, sort_method)()

    is_price_sort = "low" in sort_method or "high" in sort_method

    if is_price_sort:
        prices = products_page.get_all_product_prices()
        print("FINAL:", prices, "SORTED:", sorted(prices, reverse=reverse))
        assert prices == sorted(prices, reverse=reverse)
    else:
        names = products_page.get_all_product_names()
        print("FINAL:", names, "SORTED:", sorted(names, reverse=reverse))
        assert names == sorted(names, reverse=reverse)


@pytest.mark.ui
def test_scroll_up_down(products_page):
    assert products_page.get_page_title() == "PRODUCTS", "Should start on PRODUCTS page"
    
    for _ in range(3):
        products_page.scroll_down()

   
    assert products_page.get_page_title() == "PRODUCTS", "Page title should remain after scrolling down"

    
    for _ in range(3):
        products_page.scroll_up()

    assert products_page.get_page_title() == "PRODUCTS", "Page title should remain after scrolling up"


@pytest.mark.functional
def test_drag_and_drop_add_to_cart(products_page):
    before = products_page.cart_badge_value()

    products_page.drag_first_product_to_cart()

    after = products_page.cart_badge_value()

    assert after == before + 1, f"Badge should increase: before={before}, after={after}"
