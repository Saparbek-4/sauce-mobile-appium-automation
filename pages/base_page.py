from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from utils.logger import logger
import utils.waits as waits

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        logger.info(f"Initialized page object: {self.__class__.__name__}")

    # ========= Core Interaction Methods ========= #

    def find(self, locator):
        """Return element when it becomes visible on screen."""
        logger.info(f"Finding element: {locator}")
        try:
            element = waits.wait_for_visible(self.driver, locator)
            logger.info(f"Element found: {locator}")
            return element
        except Exception as e:
            logger.error(f"Element NOT found: {locator} — {e}")
            raise

    def find_all(self, locator):
        logger.info(f"Finding elements: {locator}")
        elements = self.driver.find_elements(*locator)
        logger.info(f"Found {len(elements)} elements for {locator}")
        return elements

    def tap(self, locator_or_element):
        """Click on an element or locator."""
        if isinstance(locator_or_element, tuple):
            logger.info(f"Tapping element by locator: {locator_or_element}")
            el = self.find(locator_or_element)
        else:
            logger.info(f"Tapping WebElement directly")
            el = locator_or_element

        try:
            el.click()
            logger.info("Tap successful")
        except Exception as e:
            logger.error(f"Tap FAILED: {e}")
            raise
        
    def count(self, locator):
        """Return number of matching elements."""
        logger.info(f"Counting elements: {locator}")
        count = len(self.driver.find_elements(*locator))
        logger.info(f"Count result: {count}")
        return count

    def type(self, locator, value: str):
        """Clear and type text into input."""
        logger.info(f"Typing '{value}' into {locator}")
        try:
            el = self.find(locator)
            el.clear()
            el.send_keys(value)
            logger.info("Typing successful")
            return el
        except Exception as e:
            logger.error(f"Typing FAILED: {e}")
            raise

    def get_text(self, locator):
        """Get element text."""
        logger.info(f"Getting text from: {locator}")
        try:
            text = waits.wait_for_visible(self.driver, locator).text
            logger.info(f"Received text: '{text}'")
            return text
        except Exception as e:
            logger.error(f"Failed to get text: {locator} — {e}")
            raise

    def get_error(self):
        """Get login error message."""
        locator = (AppiumBy.XPATH, "//.[@content-desc='test-Error message']//android.widget.TextView")
        return self.get_text(locator)

    def is_visible(self, locator):
        """Return True if element visible, False otherwise."""
        logger.info(f"Checking visibility: {locator}")
        try:
            waits.wait_for_visible(self.driver, locator)
            logger.info("Element is visible")
            return True
        except:
            logger.warning(f"Element NOT visible: {locator}")
            return False

    # ========= Scroll Actions ========= #

    def scroll_down(self, speed=600):
        logger.info("Scrolling DOWN")
        size = self.driver.get_window_size()
        start_x = size["width"] * 0.5
        start_y = size["height"] * 0.8
        end_y   = size["height"] * 0.3

        try:
            self.driver.execute_script(
                "mobile: dragGesture",
                {"startX": start_x, "startY": start_y, "endX": start_x, "endY": end_y, "speed": speed}
            )
            logger.info("Scroll down successful")
        except Exception as e:
            logger.error(f"Scroll down FAILED: {e}")
            raise
        return True

    def scroll_up(self, speed=600):
        logger.info("Scrolling UP")
        size = self.driver.get_window_size()
        start_x = size["width"] * 0.5
        start_y = size["height"] * 0.3
        end_y   = size["height"] * 0.8

        try:
            self.driver.execute_script(
                "mobile: dragGesture",
                {
                    "startX": start_x, 
                    "startY": start_y, 
                    "endX": start_x, 
                    "endY": end_y, 
                    "speed": speed
                }
            )
            logger.info("Scroll up successful")
        except Exception as e:
            logger.error(f"Scroll up FAILED: {e}")
            raise
        return True

    # ========= Drag & Drop ========= #

    def drag_and_drop(self, element, target):
        logger.info(f"Drag & drop from {element} to {target}")
        try:
            self.driver.execute_script(
                "mobile: dragGesture",
                {
                    "startX": element.location['x'] + element.size['width'] / 2,
                    "startY": element.location['y'] + element.size['height'] / 2,
                    "endX": target.location['x'] + target.size['width'] / 2,
                    "endY": target.location['y'] + target.size['height'] / 2,
                    "speed": 600
                }
            )
            logger.info("Drag & drop successful")
        except Exception as e:
            logger.error(f"Drag & drop FAILED: {e}")
            raise

    def find_in_scroll(self, locator, max_swipes=6):
        logger.info(f"Searching for element with scrolling: {locator}")
        for i in range(max_swipes):
            elements = self.find_all(locator)
            if elements:
                logger.info(f"Element found after {i} scrolls")
                return elements[0]
            logger.info("Element not found, scrolling down")
            self.scroll_down()

        logger.error(f"Element NOT found after {max_swipes} scrolls: {locator}")
        raise Exception(f"Element {locator} not found even after scrolling")
