import os
import allure
import pytest
from appium import webdriver
from pages.native_apk_pages.create_task_page import CreateTaskPage
from pages.native_apk_pages.main_page import MainPage
from pages.native_apk_pages.task_page import TaskPage
from support.desired_capabilities import DesiredCapabilities
from support.links import hub_link


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
    browser = webdriver.Remote(hub_link, DesiredCapabilities.mobileCapabilities)
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.fixture(scope='module')
def main_page(browser):
    main_page = MainPage(browser)
    yield main_page


@pytest.fixture(scope='module')
def task_page(browser):
    task_page = TaskPage(browser)
    yield task_page


@pytest.fixture(scope='module')
def create_task_page(browser):
    create_task_page = CreateTaskPage(browser)
    yield create_task_page
