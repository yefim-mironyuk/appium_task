import pytest
from support.generated_data import *


@pytest.fixture(scope="module", autouse=True)
def setup(main_page, create_task_page):
    main_page.click_create_task_button()
    create_task_page.fill_title_field(generated_title)
    create_task_page.fill_description_field(generated_description)
    create_task_page.click_save_task_button()


def test_create_task(main_page):
    main_page.is_new_task_title_correct(generated_title)


def test_rename_title(main_page, task_page):
    main_page.go_to_task_page()
    task_page.rename_title(new_title)
    task_page.click_save_changes_button()
    main_page.is_title_renamed(new_title)


def test_title_should_be_not_empty(main_page, task_page):
    main_page.go_to_task_page()
    task_page.clear_title()
    task_page.click_save_changes_button()
    task_page.should_be_error_message()
