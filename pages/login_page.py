from pages.base_page import BasePage
from locators.login_locators import LoginLocators

class LoginPage(BasePage):
    def login(self, username, password):
        self.send_keys(*LoginLocators.USERNAME, value=username)
        self.send_keys(*LoginLocators.PASSWORD, value=password)
        self.click(*LoginLocators.LOGIN_BTN)

    def is_error_displayed(self):
        return self.is_displayed(*LoginLocators.ERROR_MSG)
