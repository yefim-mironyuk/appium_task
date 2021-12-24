from .base_page import BasePage
from support.browser_helper import ElementInteractions as EI
from .locators import CreateRepositoryPageLocators


class CreateRepositoryPage(BasePage):
    def create_repository(self, name):
        EI.send_keys_in_field(EI(self.browser), *CreateRepositoryPageLocators.REPOSITORY_NAME_FIELD, name)
        EI.click_an_element(EI(self.browser), *CreateRepositoryPageLocators.CREATE_REPOSITORY_BUTTON)
