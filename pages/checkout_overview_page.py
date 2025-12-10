from pages.base_page import BasePage
from locators.checkout_locators import CheckoutLocators
from pages.checkout_complete_page import CheckoutCompletePage
from utils.logger import logger


class CheckoutOverviewPage(BasePage):

    def is_loaded(self):
        logger.info("Checking if Checkout Overview page is loaded")
        loaded = self.is_visible(CheckoutLocators.OVERVIEW_TITLE)
        logger.info(f"Checkout Overview page loaded: {loaded}")
        return loaded

    def finish(self):
        logger.info("Looking for FINISH button (scroll if necessary)")
        try:
            self.find_in_scroll(CheckoutLocators.FINISH_BTN)
            logger.info("FINISH button found — clicking")
            self.tap(CheckoutLocators.FINISH_BTN)
        except Exception as e:
            logger.error(f"Failed to click FINISH: {e}")
            raise

        logger.info("Navigating to Checkout Complete page")
        return CheckoutCompletePage(self.driver)

    def cancel(self):
        logger.info("Cancelling checkout process")
        self.tap(CheckoutLocators.CANCEL_BTN)

    def get_totals(self):
        logger.info("Reading totals from checkout overview")

        try:
            self.find_in_scroll(CheckoutLocators.TAX)
            totals = {
                "item_total": self.get_text(CheckoutLocators.ITEM_TOTAL),
                "tax": self.get_text(CheckoutLocators.TAX),
                "total": self.get_text(CheckoutLocators.TOTAL)
            }
            logger.info(f"Totals collected: {totals}")
            return totals

        except Exception as e:
            logger.error(f"Failed to read totals: {e}")
            raise
