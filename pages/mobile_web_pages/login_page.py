from pages.mobile_web_pages.base_page import BasePage
from pages.mobile_web_pages.locators import LoginPageLocators
from support.browser_helper import ElementInteractions as EI


class LoginPage(BasePage):
    def fill_username_field(self, text):
        EI.send_keys_in_field(EI(self.browser), *LoginPageLocators.USERNAME_FIELD, text)

    def fill_password_field(self, text):
        EI.send_keys_in_field(EI(self.browser), *LoginPageLocators.PASSWORD_FIELD, text)

    def click_sign_in_button(self):
        EI.click_element(EI(self.browser), *LoginPageLocators.SIGN_IN_BUTTON)

