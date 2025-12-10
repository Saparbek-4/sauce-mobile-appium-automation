# import pytest, time

# @pytest.mark.session
# def test_session_persistence(driver, products_page):
#     # Kill app
#     driver.terminate_app("com.swaglabsmobileapp")

#     # Restart
#     driver.activate_app("com.swaglabsmobileapp")

#     # User should remain logged in
#     assert products_page.is_loaded(), "User should remain logged in after restart"


# @pytest.mark.network
# def test_login_no_network(driver):
#     driver.set_network_connection(0)  # offline

#     login = LoginPage(driver)
#     login.login("standard_user", "secret_sauce")

#     assert login.get_error() == "Problem authenticating user", \
#         "Login error should appear when offline"

#     driver.set_network_connection(6)  # restore full network
    

# @pytest.mark.stability
# def test_fast_scrolling(products_page):
#     for _ in range(10):
#         products_page.scroll_down(10000)
#         products_page.scroll_up(10000)

#     # UI still operational
#     assert products_page.is_loaded()
