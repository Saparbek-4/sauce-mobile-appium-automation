from pages.base_page import BasePage
from pages.cart_page import CartPage
from pages.menu_page import MenuPage
from locators.products_locators import ProductsLocators
from locators.menu_locators import MenuLocators
from utils.logger import logger


class ProductsPage(BasePage):

    # =================== PAGE STATE =================== #

    def is_loaded(self):
        logger.info("Checking if Products page is loaded")
        loaded = self.is_visible(ProductsLocators.TITLE)
        logger.info(f"Products page loaded: {loaded}")
        return loaded

    def get_page_title(self):
        logger.info("Getting Products page title")
        return self.get_text(ProductsLocators.TITLE)

    def product_count(self):
        logger.info("Counting product cards")
        return self.count(ProductsLocators.PRODUCT_CARD)

    # =================== ADD / REMOVE PRODUCTS =================== #

    def add_product_to_cart(self, product_name):
        logger.info(f"Adding product to cart: {product_name}")
        locator = ProductsLocators.get_add_to_cart_for_product(product_name)

        try:
            button = self.find_in_scroll(locator)
            self.tap(button)
            logger.info(f"Product successfully added: {product_name}")
        except Exception as e:
            logger.error(f"Failed to add product {product_name}: {e}")
            raise

    def remove_product_from_cart(self, product_name):
        logger.info(f"Removing product from cart: {product_name}")
        try:
            self.tap(ProductsLocators.get_remove_button_for_product(product_name))
        except Exception as e:
            logger.error(f"Failed to remove product {product_name}: {e}")
            raise

    # =================== SORTING =================== #

    def open_sort(self):
        logger.info("Opening sort dropdown")
        self.tap(ProductsLocators.SORT_BUTTON)

    def sort_by_az(self):
        logger.info("Sorting products A → Z")
        self.open_sort()
        self.tap(ProductsLocators.SORT_OPTION_AZ)

    def sort_by_za(self):
        logger.info("Sorting products Z → A")
        self.open_sort()
        self.tap(ProductsLocators.SORT_OPTION_ZA)

    def sort_by_low_high(self):
        logger.info("Sorting products Low → High")
        self.open_sort()
        self.tap(ProductsLocators.SORT_OPTION_LOHI)

    def sort_by_high_low(self):
        logger.info("Sorting products High → Low")
        self.open_sort()
        self.tap(ProductsLocators.SORT_OPTION_HILO)

    # =================== SCROLL COLLECTION =================== #

    def get_all_product_names(self):
        logger.info("Collecting ALL product names (with scrolling)")
        collected = []
        seen = set()
        last_count = -1

        while True:
            elements = self.find_all(ProductsLocators.PRODUCT_NAME)

            for el in elements:
                name = el.text.strip()
                if name and name not in seen:
                    seen.add(name)
                    collected.append(name)
                    logger.debug(f"Found product: {name}")

            if len(collected) == last_count:
                break  # no new names → stop

            last_count = len(collected)

            if not self.scroll_down():
                break

        logger.info(f"Collected product names: {collected}")
        return collected

    def get_all_product_prices(self):
        logger.info("Collecting ALL product prices (with scrolling)")
        collected = []
        seen = set()
        last_count = -1

        while True:
            cards = self.find_all(ProductsLocators.PRODUCT_CARD)

            for card in cards:
                try:
                    title_el = card.find_element(*ProductsLocators.PRODUCT_NAME)
                    price_el = card.find_element(*ProductsLocators.PRODUCT_PRICE)

                    title = title_el.text.strip()
                    price_text = price_el.text.strip()

                    if not price_text.startswith("$"):
                        continue

                    price = float(price_text.replace("$", ""))

                    if title not in seen:
                        seen.add(title)
                        collected.append(price)
                        logger.debug(f"Found price: {title} → {price}")

                except Exception:
                    continue  # skip malformed card

            if len(collected) == last_count:
                break

            last_count = len(collected)
            if not self.scroll_down():
                break

        logger.info(f"Collected prices: {collected}")
        return collected

    # =================== CART BADGE =================== #

    def cart_badge_value(self):
        logger.info("Reading cart badge value")
        try:
            value = int(self.get_text(ProductsLocators.CART_BADGE))
            logger.info(f"Cart badge = {value}")
            return value
        except:
            logger.warning("Cart badge not found, returning 0")
            return 0

    # =================== DnD ACTION =================== #

    def drag_first_product_to_cart(self):
        logger.info("Dragging first product into cart (DnD)")

        drag_handle = self.find(ProductsLocators.DRAG_HANDLE)
        drop_zone = self.find(ProductsLocators.DRAG_ZONE)

        self.drag_and_drop(drag_handle, drop_zone)

    # =================== NAVIGATION =================== #

    def open_menu(self):
        logger.info("Opening side menu")
        self.tap(MenuLocators.MENU_BUTTON)
        return MenuPage(self.driver)

    def open_cart(self):
        logger.info("Opening cart")
        self.tap(ProductsLocators.CART_ICON)

        return CartPage(self.driver)
