from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.timeout = timeout

    def find(self, by, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located((by, locator))
        )

    def click(self, by, locator):
        el = self.find(by, locator)
        el.click()

    def send_keys(self, by, locator, value):
        el = self.find(by, locator)
        el.clear()
        el.send_keys(value)

    def is_displayed(self, by, locator):
        try:
            el = self.find(by, locator)
            return el.is_displayed()
        except Exception:
            return False
