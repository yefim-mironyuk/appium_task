from pages.mobile_web_pages.locators import ChromeStartPageLocators
from support.browser_helper import ElementInteractions as EI


class ChromeStartPage:
    def __init__(self, browser):
        self.browser = browser

    def switch_to_native(self):
        native = self.browser.contexts[0]
        self.browser.switch_to.context(native)

    def skip_welcome_page(self):
        EI.click_an_element(EI(self.browser), *ChromeStartPageLocators.TERMS_ACCEPT_BUTTON)
        EI.click_an_element(EI(self.browser), *ChromeStartPageLocators.DONT_SEND_DATA_BUTTON)
