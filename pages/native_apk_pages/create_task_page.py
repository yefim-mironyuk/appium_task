from pages.native_apk_pages.locators import CreateTaskPageLocators
from pages.native_apk_pages.base_page import BasePage
from support.browser_helper import ElementInteractions as EI


class CreateTaskPage(BasePage):
    def fill_title_field(self, message):
        EI.send_keys_in_field(EI(self.browser), *CreateTaskPageLocators.NEW_TASK_TITLE_FIELD, message)
        EI.hide_keyboard(EI(self.browser))

    def fill_description_field(self, message):
        EI.send_keys_in_field(EI(self.browser), *CreateTaskPageLocators.NEW_TASK_DESCRIPTION_FIELD, message)
        EI.hide_keyboard(EI(self.browser))

    def click_save_task_button(self):
        EI.click_an_element(EI(self.browser), *CreateTaskPageLocators.SAVE_NEW_TASK_BUTTON)
