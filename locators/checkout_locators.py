from appium.webdriver.common.appiumby import AppiumBy

class CheckoutLocators:

    # Cart page
    CHECKOUT_BTN = (AppiumBy.ACCESSIBILITY_ID, "test-CHECKOUT")

    # Information page
    INFO_TITLE = (AppiumBy.XPATH, "//*[@text='CHECKOUT: INFORMATION']")
    FIRST_NAME = (AppiumBy.ACCESSIBILITY_ID, "test-First Name")
    LAST_NAME = (AppiumBy.ACCESSIBILITY_ID, "test-Last Name")
    ZIP = (AppiumBy.ACCESSIBILITY_ID, "test-Zip/Postal Code")
    CONTINUE_BTN = (AppiumBy.ACCESSIBILITY_ID, "test-CONTINUE")
    ERROR_MSG = (AppiumBy.XPATH, "//.[@content-desc='test-Error message']//android.widget.TextView")

    # Overview page
    OVERVIEW_TITLE = (AppiumBy.XPATH, "//*[@text='CHECKOUT: OVERVIEW']")
    FINISH_BTN = (AppiumBy.ACCESSIBILITY_ID, "test-FINISH")
    CANCEL_BTN = (AppiumBy.ACCESSIBILITY_ID, "test-CANCEL")
    ITEM_TOTAL = (AppiumBy.XPATH, "//*[contains(@text, 'Item total')]")
    TAX = (AppiumBy.XPATH, "//*[contains(@text, 'Tax')]")
    TOTAL = (AppiumBy.XPATH, "//*[contains(@text, 'Total')]")

    # Complete page
    COMPLETE_TITLE = (AppiumBy.ACCESSIBILITY_ID, "test-CHECKOUT: COMPLETE!")
