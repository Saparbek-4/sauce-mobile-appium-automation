import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = logging.getLogger("framework.waits")


# ---------- Core Waits ---------- #

def wait_for_element(driver, locator, timeout=15):
    """Wait until element is present in DOM."""
    logger.info(f"[WAIT] presence of element: {locator}")
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located(locator)
    )


def wait_for_visible(driver, locator, timeout=15):
    """Wait until element becomes visible."""
    logger.info(f"[WAIT] visibility of element: {locator}")
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(locator)
    )


def wait_for_clickable(driver, locator, timeout=15):
    """Wait until element can be clicked."""
    logger.info(f"[WAIT] clickable element: {locator}")
    return WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(locator)
    )


def wait_for_invisible(driver, locator, timeout=15):
    """Wait until element disappears from the screen."""
    logger.info(f"[WAIT] invisibility of element: {locator}")
    return WebDriverWait(driver, timeout).until(
        EC.invisibility_of_element_located(locator)
    )


def wait_for_text(driver, locator, text, timeout=15):
    """Wait until element contains specific text."""
    logger.info(f"[WAIT] text '{text}' in element: {locator}")
    return WebDriverWait(driver, timeout).until(
        EC.text_to_be_present_in_element(locator, text)
    )

