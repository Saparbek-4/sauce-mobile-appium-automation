from appium.webdriver.common.appiumby import AppiumBy

class LoginLocators:
    USERNAME_FIELD = (AppiumBy.ACCESSIBILITY_ID, "test-Username")
    PASSWORD_FIELD = (AppiumBy.ACCESSIBILITY_ID, "test-Password")
    LOGIN_BUTTON   = (AppiumBy.ACCESSIBILITY_ID, "test-LOGIN")

    ERROR_MESSAGE  = (AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='test-Error message']//android.widget.TextView")