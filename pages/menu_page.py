from locators.menu_locators import MenuLocators
from pages.base_page import BasePage
from utils.logger import logger
import utils.waits as waits

class MenuPage(BasePage):

    def is_loaded(self) -> bool:
        logger.info("Checking if Menu is loaded")
        loaded = self.is_visible(MenuLocators.MENU_CLOSE_BUTTON)
        logger.info(f"Menu loaded: {loaded}")
        return loaded

    def open_menu(self) -> None:
        logger.info("Opening menu")
        try:
            self.tap(MenuLocators.MENU_BUTTON)
            logger.info("Menu button tapped")
        except Exception as e:
            logger.error(f"Failed to open menu: {e}")
            raise

    def is_closed(self) -> bool:
        logger.info("Checking if Menu is closed")
        try:
            closed = waits.wait_for_invisible(self.driver, MenuLocators.MENU_CLOSE_BUTTON)
            logger.info(f"Menu closed: {closed}")
            return closed
        except Exception as e:
            logger.error(f"Error when checking menu closed state: {e}")
            return False

    def close_menu(self) -> None:
        logger.info("Closing menu")
        try:
            self.tap(MenuLocators.MENU_CLOSE_BUTTON)
            waits.wait_for_invisible(self.driver, MenuLocators.MENU_CLOSE_BUTTON)
            logger.info("Menu closed")
        except Exception as e:
            logger.error(f"Failed to close menu: {e}")
            raise

    def logout(self) -> None:
        logger.info("Clicking logout in menu")
        try:
            self.tap(MenuLocators.MENU_ITEM_LOGOUT)
            logger.info("Logout clicked")
        except Exception as e:
            logger.error(f"Failed to click logout: {e}")
            raise

    def reset_app_state(self) -> None:
        logger.info("Resetting app state via menu")
        try:
            self.tap(MenuLocators.MENU_ITEM_RESET)
            logger.info("Reset action performed, closing menu")
            self.close_menu()
        except Exception as e:
            logger.error(f"Failed to reset app state: {e}")
            raise

    def get_menu_items(self) -> list:
        """
        Return visible menu item texts.
        """
        logger.info("Collecting menu item texts")
        texts = []
        locators = [
            MenuLocators.MENU_ITEM_ALL_ITEMS,
            MenuLocators.MENU_ITEM_RESET,
            MenuLocators.MENU_ITEM_LOGOUT,
        ]

        for loc in locators:
            try:
                if self.is_visible(loc):
                    text = self.get_text(loc)
                    texts.append(text)
                    logger.info(f"Found menu item: {text}")
                else:
                    logger.debug(f"Menu item not visible for locator: {loc}")
            except Exception as e:
                logger.warning(f"Failed to read menu item {loc}: {e}")

        logger.info(f"Collected menu items: {texts}")
        return texts
