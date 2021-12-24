from utils.logging import Logger


class BasePage(Logger):
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def switch_to_web(self):
        web = self.browser.contexts[-1]
        self.browser.switch_to.context(web)

    def switch_to_native(self):
        native = self.browser.contexts[0]
        self.browser.switch_to.context(native)