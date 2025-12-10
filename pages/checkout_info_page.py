from pages.base_page import BasePage
from locators.checkout_locators import CheckoutLocators
from pages.checkout_overview_page import CheckoutOverviewPage
from utils.logger import logger


class CheckoutInfoPage(BasePage):

    def is_loaded(self):
        logger.info("Checking if Checkout Info page is loaded")
        loaded = self.is_visible(CheckoutLocators.INFO_TITLE)
        logger.info(f"Checkout Info page loaded: {loaded}")
        return loaded

    def fill_form(self, first, last, zip_code):
        logger.info(f"Filling checkout form: {first} {last}, zip={zip_code}")

        try:
            self.type(CheckoutLocators.FIRST_NAME, first)
            self.type(CheckoutLocators.LAST_NAME, last)
            self.type(CheckoutLocators.ZIP, zip_code)
            logger.info("Checkout form filled successfully")
        except Exception as e:
            logger.error(f"Failed to fill checkout form: {e}")
            raise

    def submit(self):
        logger.info("Submitting checkout info form")
        self.tap(CheckoutLocators.CONTINUE_BTN)
        logger.info("Navigating to Checkout Overview page")
        return CheckoutOverviewPage(self.driver)
