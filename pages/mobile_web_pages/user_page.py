from pages.mobile_web_pages.base_page import BasePage
from pages.mobile_web_pages.locators import UserPageLocators
from support.browser_helper import ElementInteractions as EI


class UserPage(BasePage):
    def open_repositories(self):
        EI.click_element(EI(self.browser), *UserPageLocators.REPOSITORIES_BUTTON)

    def go_to_create_repository_page(self):
        EI.click_element(EI(self.browser), *UserPageLocators.NEW_REPOSITORY_BUTTON)

