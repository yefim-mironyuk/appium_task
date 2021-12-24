from pages.mobile_web_pages.base_page import BasePage
from pages.mobile_web_pages.locators import LoginPageLocators
from support.browser_helper import ElementInteractions as EI


class LoginPage(BasePage):
    def fill_username_field(self, username):
        EI.send_keys_in_field(EI(self.browser), *LoginPageLocators.USERNAME_FIELD, username)

    def fill_password_field(self, password):
        EI.send_keys_in_field(EI(self.browser), *LoginPageLocators.PASSWORD_FIELD, password)

    def click_sign_in_button(self):
        EI.click_an_element(EI(self.browser), *LoginPageLocators.SIGN_IN_BUTTON)

