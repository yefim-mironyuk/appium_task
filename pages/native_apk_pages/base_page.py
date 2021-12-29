from utils.logging import Logger


class BasePage(Logger):
    def __init__(self, browser):
        self.browser = browser
