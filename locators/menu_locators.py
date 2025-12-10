from appium.webdriver.common.appiumby import AppiumBy


class MenuLocators:
    MENU_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "test-Menu")
    MENU_CLOSE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "test-Close")
    MENU_ITEM_LOGOUT = (AppiumBy.ACCESSIBILITY_ID, "test-LOGOUT")
    MENU_ITEM_RESET =  (AppiumBy.ACCESSIBILITY_ID, "test-RESET APP STATE")
    MENU_ITEM_ALL_ITEMS = (AppiumBy.ACCESSIBILITY_ID, "test-ALL ITEMS")
