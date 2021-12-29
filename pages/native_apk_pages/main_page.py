from pages.native_apk_pages.locators import MainPageLocators
from pages.native_apk_pages.base_page import BasePage
from support.browser_helper import ElementInteractions as EI
from utils.assertions import *


class MainPage(BasePage):
    def click_create_task_button(self):
        EI.click_element(EI(self.browser), *MainPageLocators.CREATE_NEW_TASK_BUTTON)

    def is_new_task_title_correct(self, new_task_title):
        new_task_title_on_main_page = EI.find_visible_element(EI(self.browser),
                                                              *MainPageLocators.NEW_TASK_ON_MAIN_PAGE).text
        are_objects_equal(new_task_title_on_main_page, new_task_title)

    def go_to_task_page(self):
        EI.click_element(EI(self.browser), *MainPageLocators.NEW_TASK_ON_MAIN_PAGE)

    def is_title_renamed(self, renamed_title):
        task_title_on_main_page = EI.find_visible_element(EI(self.browser),
                                                          *MainPageLocators.NEW_TASK_ON_MAIN_PAGE).text
        are_objects_equal(task_title_on_main_page, renamed_title)
