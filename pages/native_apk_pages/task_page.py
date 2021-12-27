from pages.native_apk_pages.locators import TaskPageLocators
from pages.native_apk_pages.base_page import BasePage
from support.browser_helper import ElementInteractions as EI


class TaskPage(BasePage):
    def rename_title(self, text):
        EI.send_keys_in_field(EI(self.browser), *TaskPageLocators.TITLE_FIELD, text)
        EI.hide_keyboard(EI(self.browser))

    def click_save_changes_button(self):
        EI.click_an_element(EI(self.browser), *TaskPageLocators.SAVE_CHANGES_BUTTON)

    def clear_title(self):
        EI.clear_field(EI(self.browser), *TaskPageLocators.TITLE_FIELD)
        EI.hide_keyboard(EI(self.browser))

    def should_be_error_message(self):
        EI.is_element_present(EI(self.browser), *TaskPageLocators.ERROR_MESSAGE)
