from utils.assertions import are_objects_equal
from .base_page import BasePage
from support.browser_helper import ElementInteractions as EI
from .locators import RepositoryPageLocators


class RepositoryPage(BasePage):
    def is_repository_created(self):
        EI.is_element_present(EI(self.browser), *RepositoryPageLocators.QUICK_SETUP_MESSAGE)

    def is_repository_name_correct(self, name):
        repository_name_on_page = EI.find_visible_element(EI(self.browser),
                                                          *RepositoryPageLocators.REPOSITORY_NAME).text
        are_objects_equal(repository_name_on_page, name)

    def go_to_settings_page(self):
        EI.click_element(EI(self.browser), *RepositoryPageLocators.SETTINGS_BUTTON)

    def is_repository_renamed(self, new_name):
        rename_repository_name_on_page = EI.find_visible_element(EI(self.browser),
                                                                 *RepositoryPageLocators.REPOSITORY_NAME).text
        are_objects_equal(rename_repository_name_on_page, new_name)
