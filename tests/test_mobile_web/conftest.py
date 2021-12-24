import os
import allure
import pytest
from appium import webdriver
from pages.mobile_web_pages.chrome_start_page import ChromeStartPage
from pages.mobile_web_pages.login_page import LoginPage
from pages.mobile_web_pages.main_page import MainPage
from pages.mobile_web_pages.create_repository_page import CreateRepositoryPage
from pages.mobile_web_pages.repository_page import RepositoryPage
from pages.mobile_web_pages.repository_settings_page import RepositorySettingsPage
from pages.mobile_web_pages.user_page import UserPage
from support.desired_capabilities import DesiredCapabilities
from support.links import start_link as link


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        mode = 'a' if os.path.exists('failures') else 'w'
        try:
            with open('failures', mode) as f:
                if 'browser' in item.fixturenames:
                    web_driver = item.funcargs['browser']
                else:
                    print('Fail to take screen-shot')
                    return
            allure.attach(
                web_driver.get_screenshot_as_png(),
                name='screenshot',
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            print('Fail to take screen-shot: {}'.format(e))


@pytest.fixture(scope="module")
def browser():
    browser = webdriver.Remote("http://localhost:4723/wd/hub", DesiredCapabilities.webCapabilities)
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.fixture(scope='module')
def chrome_start_page(browser):
    chrome_start_page = ChromeStartPage(browser)
    yield chrome_start_page


@pytest.fixture(scope='module')
def login_page(browser):
    login_page = LoginPage(browser, link)
    yield login_page


@pytest.fixture(scope='module')
def main_page(browser):
    main_page = MainPage(browser, link)
    yield main_page


@pytest.fixture(scope='module')
def user_page(browser):
    user_page = UserPage(browser, link)
    yield user_page


@pytest.fixture(scope='module')
def create_repository_page(browser):
    create_repository_page = CreateRepositoryPage(browser, link)
    yield create_repository_page


@pytest.fixture(scope='module')
def repository_page(browser):
    repository_page = RepositoryPage(browser, link)
    yield repository_page


@pytest.fixture(scope='module')
def repository_settings_page(browser):
    repository_settings_page = RepositorySettingsPage(browser, link)
    yield repository_settings_page
