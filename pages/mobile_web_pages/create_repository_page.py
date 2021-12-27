from .base_page import BasePage
from support.browser_helper import ElementInteractions as EI
from .locators import CreateRepositoryPageLocators


class CreateRepositoryPage(BasePage):
    def create_repository(self, text):
        EI.send_keys_in_field(EI(self.browser), *CreateRepositoryPageLocators.REPOSITORY_NAME_FIELD, text)
        EI.click_element(EI(self.browser), *CreateRepositoryPageLocators.CREATE_REPOSITORY_BUTTON)
