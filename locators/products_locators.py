from appium.webdriver.common.appiumby import AppiumBy

class ProductsLocators:
    TITLE = (AppiumBy.XPATH, "//android.widget.TextView[@text='PRODUCTS']")
    PRODUCT_CARD = (AppiumBy.XPATH, "//*[@content-desc='test-Item']")

    PRODUCT_NAME = (AppiumBy.XPATH, ".//*[@content-desc='test-Item title']")
    PRODUCT_PRICE = (AppiumBy.XPATH, ".//*[@content-desc='test-Price']")

    
    @staticmethod
    def get_add_to_cart_for_product(product_name: str):
        return (
            AppiumBy.XPATH,
            f"//*[@content-desc='test-Item title'][@text='{product_name}']"
            "/../..//*[@content-desc='test-ADD TO CART']"
    )
        
    @staticmethod
    def get_remove_button_for_product(product_name: str):
        return (
            AppiumBy.XPATH,
            f"//*[@content-desc='test-Item title'][@text='{product_name}']"
            "/../..//*[@content-desc='test-REMOVE']"
    )
    SORT_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "test-Modal Selector Button")
    SORT_OPTION_AZ = (AppiumBy.XPATH, "//*[@text='Name (A to Z)']")
    SORT_OPTION_ZA = (AppiumBy.XPATH, "//*[@text='Name (Z to A)']")
    SORT_OPTION_LOHI = (AppiumBy.XPATH, "//*[@text='Price (low to high)']")
    SORT_OPTION_HILO = (AppiumBy.XPATH, "//*[@text='Price (high to low)']")

    CART_BADGE = (
        AppiumBy.XPATH,
        "//*[@content-desc='test-Cart']//android.widget.TextView"
    ) 

    CART_ICON = (AppiumBy.ACCESSIBILITY_ID, "test-Cart")

    DRAG_ZONE = (AppiumBy.ACCESSIBILITY_ID, "test-Cart drop zone")
    DRAG_HANDLE = (AppiumBy.ACCESSIBILITY_ID, "test-Drag Handle")

