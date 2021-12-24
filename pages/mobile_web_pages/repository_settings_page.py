from .base_page import BasePage
from .locators import *
from support.browser_helper import ElementInteractions as EI


class RepositorySettingsPage(BasePage):
    def delete_repository(self):
        EI.click_an_element(EI(self.browser), *RepositorySettingsPageLocators.DELETE_REPOSITORY_BUTTON)
        deleting_message = EI.find_visible_element(EI(self.browser), *RepositorySettingsPageLocators.PLEASE_TYPE_MESSAGE).text
        EI.send_keys_in_field(EI(self.browser), *RepositorySettingsPageLocators.INPUT_FIELD, deleting_message)
        EI.click_an_element(EI(self.browser), *RepositorySettingsPageLocators.I_UNDERSTAND_BUTTON)

    def rename_repository(self, new_title):
        EI.send_keys_in_field(EI(self.browser), *RepositorySettingsPageLocators.RENAME_REPOSITORY_FIELD, new_title)
        EI.click_an_element(EI(self.browser), *RepositorySettingsPageLocators.RENAME_BUTTON)

