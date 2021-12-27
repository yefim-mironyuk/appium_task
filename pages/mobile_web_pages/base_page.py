from utils.logging import Logger
from support.config import ContextsConstants


class BasePage(Logger):
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def switch_to_context(self, context_name):
        web = self.browser.contexts[ContextsConstants.web_id]
        native = self.browser.contexts[ContextsConstants.native_id]
        if context_name == "web":
            self.browser.switch_to.context(web)
        elif context_name == "native":
            self.browser.switch_to.context(native)
