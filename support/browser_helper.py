from loguru import logger
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class ElementInteractions:
    def __init__(self, browser):
        self.browser = browser

    def find_visible_element(self, strategy, selector):
        logger.debug(f'Trying to find visible element "{strategy}", "{selector}"...')
        try:
            element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((strategy, selector)))
        except Exception:
            logger.error(f'Cannot find visible element "{strategy}", "{selector}"!')
            raise
        logger.debug(f'Element "{strategy}", "{selector}" was found...')
        return element

    def click_an_element(self, strategy, selector):
        logger.debug(f'Trying to find clickable element "{strategy}", "{selector}"...')
        try:
            element = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((strategy, selector)))
        except Exception:
            logger.error(f'Cannot find element "{strategy}", "{selector}"...')
            raise
        logger.debug(f'Clickable element "{strategy}", "{selector}" was found...')
        logger.debug(f'Trying to click an element "{strategy}", "{selector}"...')
        try:
            element.click()
        except Exception:
            logger.error(f'Cannot click an element "{strategy}", "{selector}"...')
            raise
        logger.debug(f'Element "{strategy}", "{selector}" clicked...')

    def send_keys_in_field(self, strategy, selector, text):
        element = self.find_visible_element(strategy, selector)
        element.clear()
        logger.debug(f'Trying to send "{text}" in element "{strategy}", "{selector}"...')
        try:
            element.send_keys(text)
        except Exception:
            logger.error(f'Cannot send {text} in element "{strategy}", "{selector}"...')
            raise
        logger.debug(f'{text} is sent in element "{strategy}", "{selector}"...')
        logger.debug(f'Hiding keyboard...')

    def clear_field(self, strategy, selector):
        element = self.find_visible_element(strategy, selector)
        element.clear()
        logger.debug(f'Field, located "{strategy}", "{selector}" cleared...')
        logger.debug(f'Hiding keyboard...')

    def hide_keyboard(self):
        self.browser.hide_keyboard()

    def is_element_present(self, strategy, selector):
        logger.debug(f'Trying to find element "{strategy}", "{selector}"...')
        try:
            WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((strategy, selector)))
        except NoSuchElementException:
            logger.error(f'Cannot find element "{strategy}", "{selector}"!')
        logger.debug(f'Element "{strategy}", "{selector}" was found...')
        return True
