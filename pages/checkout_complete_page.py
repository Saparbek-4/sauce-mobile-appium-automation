from pages.base_page import BasePage
from locators.checkout_locators import CheckoutLocators
from utils.logger import logger


class CheckoutCompletePage(BasePage):

    def is_loaded(self):
        logger.info("Checking if Checkout Complete page is loaded")
        loaded = self.is_visible(CheckoutLocators.COMPLETE_TITLE)
        logger.info(f"Checkout Complete page loaded: {loaded}")
        return loaded

    def get_title(self):
        logger.info("Getting checkout complete title text")
        text = self.get_text(CheckoutLocators.COMPLETE_TITLE)
        logger.info(f"Checkout complete title: '{text}'")
        return text
