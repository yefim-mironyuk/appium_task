from loguru import logger
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class ElementInteractions:
    def __init__(self, browser):
        self.browser = browser

    def find_visible_element(self, how, what):
        logger.debug(f'Trying to find visible element "{how}", "{what}"...')
        try:
            element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((how, what)))
        except Exception:
            logger.error(f'Cannot find visible element "{how}", "{what}"!')
            raise
        logger.debug(f'Element "{how}", "{what}" was found...')
        return element

    def click_an_element(self, how, what):
        logger.debug(f'Trying to find clickable element "{how}", "{what}"...')
        try:
            element = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((how, what)))
        except Exception:
            logger.error(f'Cannot find element "{how}", "{what}"...')
            raise
        logger.debug(f'Clickable element "{how}", "{what}" was found...')
        logger.debug(f'Trying to click an element "{how}", "{what}"...')
        try:
            element.click()
        except Exception:
            logger.error(f'Cannot click an element "{how}", "{what}"...')
            raise
        logger.debug(f'Element "{how}", "{what}" clicked...')

    def send_keys_in_field(self, how, what, message):
        element = self.click_an_element(how, what)
        element.clear()
        logger.debug(f'Trying to send "{message}" in element "{how}", "{what}"...')
        try:
            element.send_keys(message)
        except Exception:
            logger.error(f'Cannot send {message} in element "{how}", "{what}"...')
            raise
        logger.debug(f'{message} is sent in element "{how}", "{what}"...')
        logger.debug(f'Hiding keyboard...')

    def clear_field(self, how, what):
        element = self.click_an_element(how, what)
        element.clear()
        logger.debug(f'Field, located "{how}", "{what}" cleared...')
        logger.debug(f'Hiding keyboard...')

    def hide_keyboard(self):
        self.browser.hide_keyboard()

    def is_element_present(self, how, what):
        logger.info(f'Trying to find element "{how}", "{what}"...')
        try:
            WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((how, what)))
        except NoSuchElementException:
            logger.error(f'Cannot find element "{how}", "{what}"!')
        logger.debug(f'Element "{how}", "{what}" was found...')
        return True


