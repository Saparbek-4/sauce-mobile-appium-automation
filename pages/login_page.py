from pages.base_page import BasePage
from pages.products_page import ProductsPage
from locators.login_locators import LoginLocators
from utils.logger import logger


class LoginPage(BasePage):

    def is_loaded(self):
        logger.info("Checking if Login page is loaded")
        loaded = self.is_visible(LoginLocators.LOGIN_BUTTON)
        logger.info(f"Login page loaded: {loaded}")
        return loaded

    def enter_username(self, username: str):
        logger.info(f"Entering username: {username}")
        try:
            self.type(LoginLocators.USERNAME_FIELD, username)
            logger.info("Username entered successfully")
        except Exception as e:
            logger.error(f"Failed to enter username: {e}")
            raise

    def enter_password(self, password: str):
        logger.info("Entering password")
        try:
            self.type(LoginLocators.PASSWORD_FIELD, password)
            logger.info("Password entered successfully")
        except Exception as e:
            logger.error(f"Failed to enter password: {e}")
            raise

    def tap_login(self):
        logger.info("Clicking LOGIN button")
        try:
            self.tap(LoginLocators.LOGIN_BUTTON)
            logger.info("LOGIN button tapped successfully")
        except Exception as e:
            logger.error(f"Failed to tap LOGIN: {e}")
            raise

    def login(self, username: str, password: str):
        logger.info(f"Attempting login with user: {username}")

        self.enter_username(username)
        self.enter_password(password)
        self.tap_login()

        logger.info("Login submitted — navigating to ProductsPage")
        return ProductsPage(self.driver)

    def is_login_screen(self):
        visible = self.is_visible(LoginLocators.LOGIN_BUTTON)
        logger.info(f"Is login screen visible: {visible}")
        return visible
