from support.browser_helper import ElementInteractions as EI
from utils.assertions import are_objects_equal
from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def is_user_correct(self, username):
        EI.click_element(EI(self.browser), *MainPageLocators.DROPDOWN_MENU)
        username_in_menu = EI.find_visible_element(EI(self.browser), *MainPageLocators.USERNAME_IN_MENU).text
        are_objects_equal(username_in_menu, username)
        EI.click_element(EI(self.browser), *MainPageLocators.DROPDOWN_MENU)

    def go_to_user_page(self):
        EI.click_element(EI(self.browser), *MainPageLocators.DROPDOWN_MENU)
        EI.click_element(EI(self.browser), *MainPageLocators.USERNAME_IN_MENU)
