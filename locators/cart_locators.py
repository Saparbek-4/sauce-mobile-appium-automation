from appium.webdriver.common.appiumby import AppiumBy


class CartLocators:
    TITLE = (AppiumBy.XPATH, "//*[@text='YOUR CART']")
    
    ITEM_CONTAINER = (AppiumBy.ACCESSIBILITY_ID, "test-Item")
    ITEM_NAME = (AppiumBy.XPATH, ".//*[@content-desc='test-Description']/*[1]")
    ITEM_PRICE = (AppiumBy.ACCESSIBILITY_ID, "test-Price")
    
    CART_ICON = (AppiumBy.ACCESSIBILITY_ID, "test-Cart")
    PRODUCT_NAME = (AppiumBy.XPATH, "//*[@content-desc='test-Item title']")
    REMOVE_BUTTON = (AppiumBy.XPATH, "//*[@content-desc='test-REMOVE']")
    CONTINUE_SHOPPING = (AppiumBy.ACCESSIBILITY_ID, "test-CONTINUE SHOPPING")
    CHECKOUT_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "test-CHECKOUT")
