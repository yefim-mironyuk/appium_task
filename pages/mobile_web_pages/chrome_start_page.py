from pages.mobile_web_pages.locators import ChromeStartPageLocators
from support.browser_helper import ElementInteractions as EI
from pages.mobile_web_pages.base_page import BasePage


class ChromeStartPage(BasePage):

    def skip_welcome_page(self):
        EI.click_an_element(EI(self.browser), *ChromeStartPageLocators.TERMS_ACCEPT_BUTTON)
        EI.click_an_element(EI(self.browser), *ChromeStartPageLocators.DONT_SEND_DATA_BUTTON)
