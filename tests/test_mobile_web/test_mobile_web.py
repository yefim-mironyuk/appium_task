import pytest
from support.creds_constants import *
from support.generated_data import generated_title, new_title


@pytest.fixture(scope="module")
def setup(chrome_start_page, login_page):
    chrome_start_page.switch_to_native()
    chrome_start_page.skip_welcome_page()
    login_page.switch_to_web()
    login_page.open()
    login_page.fill_username_field(username)
    login_page.fill_password_field(password)
    login_page.click_sign_in_button()


def test_correct_user_is_logged_in(setup, main_page):
    main_page.is_user_correct(username)


@pytest.fixture(scope="function")
def setup_for_repositories(setup, main_page, user_page, create_repository_page, repository_page,
                           repository_settings_page):
    main_page.go_to_user_page()
    user_page.open_repositories()
    user_page.go_to_create_repository_page()
    create_repository_page.create_repository(generated_title)
    yield
    repository_page.go_to_settings_page()
    repository_settings_page.delete_repository()


def test_create_repository(setup_for_repositories, repository_page):
    repository_page.is_repository_created()
    repository_page.is_repository_name_correct(generated_title)


def test_rename_repository(setup_for_repositories, main_page, repository_settings_page, repository_page):
    repository_page.go_to_settings_page()
    repository_settings_page.rename_repository(new_title)
    repository_page.is_repository_renamed(new_title)
