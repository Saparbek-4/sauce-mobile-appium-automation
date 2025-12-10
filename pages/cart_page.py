from pages.base_page import BasePage
from locators.cart_locators import CartLocators
from utils.logger import logger


class CartPage(BasePage):

    def is_loaded(self):
        logger.info("Checking if Cart page is loaded")
        loaded = self.is_visible(CartLocators.TITLE)
        logger.info(f"Cart page loaded: {loaded}")
        return loaded

    # ========= Collect items with scrolling ========= #

    def get_products(self):
        logger.info("Collecting product names from cart (with scrolling)")

        collected = []
        seen = set()
        last_count = -1

        while True:
            elements = self.find_all(CartLocators.ITEM_CONTAINER)

            logger.info(f"Found {len(elements)} product container elements")

            for el in elements:
                try:
                    title_el = el.find_element(*CartLocators.ITEM_NAME)
                    title = title_el.text.strip()

                    if title and title not in seen:
                        seen.add(title)
                        collected.append(title)
                        logger.info(f"Collected product: {title}")

                except Exception as e:
                    logger.error(f"Failed to read product title: {e}")

            # Stop if no new elements found
            if len(collected) == last_count:
                logger.info("No new products detected — stopping scroll")
                break

            last_count = len(collected)

            # Try to scroll
            scrolled = self.scroll_down()
            if not scrolled:
                logger.warning("Unable to scroll further — stopping")
                break

        logger.info(f"Final collected product list: {collected}")
        return collected


    # ========= Actions ========= #

    def remove_first_product(self):
        logger.info("Attempting to remove first product from cart")

        buttons = self.find_all(CartLocators.REMOVE_BUTTON)

        if not buttons:
            logger.warning("REMOVE buttons not found — cart may be empty")
            return False

        try:
            buttons[0].click()
            logger.info("Successfully removed first product")
            return True
        except Exception as e:
            logger.error(f"Failed to click REMOVE: {e}")
            raise


    def continue_shopping(self):
        logger.info("Attempting to click 'Continue Shopping'")
        self.tap(CartLocators.CONTINUE_SHOPPING)
        logger.info("'Continue Shopping' clicked")


    def go_to_checkout(self):
        logger.info("Attempting to click Checkout button")
        self.tap(CartLocators.CHECKOUT_BUTTON)
        logger.info("Checkout button clicked")


    # ========= Empty State ========= #

    def is_empty(self):
        logger.info("Checking if cart is empty")
        empty = len(self.get_products()) == 0
        logger.info(f"Cart empty: {empty}")
        return empty
