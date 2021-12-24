from selenium.webdriver.common.by import By


class ChromeStartPageLocators:
    TERMS_ACCEPT_BUTTON = (By.ID, "com.android.chrome:id/terms_accept")
    DONT_SEND_DATA_BUTTON = (By.ID, "com.android.chrome:id/negative_button")


class LoginPageLocators:
    USERNAME_FIELD = (By.CSS_SELECTOR, "#login_field")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#password")
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, ".btn.btn-primary.btn-block.js-sign-in-button")


class MainPageLocators:
    DROPDOWN_MENU = (By.CSS_SELECTOR, "div:nth-child(2) > button > svg")
    USERNAME_IN_MENU = (By.CSS_SELECTOR, "nav > a:nth-child(9)")
    NEW_REPOSITORY_BUTTON = (By.CSS_SELECTOR, "#repos-container > h2 > a")
    REPOSITORY_DELETED_MESSAGE = (By.CSS_SELECTOR, "#js-flash-container > div")
    REPOSITORIES = (By.CSS_SELECTOR, "#repos-container")


class CreateRepositoryPageLocators:
    REPOSITORY_NAME_FIELD = (By.CSS_SELECTOR, "#repository_name")
    CREATE_REPOSITORY_BUTTON = (By.CSS_SELECTOR, "div.js-with-permission-fields > button")


class UserPageLocators:
    REPOSITORIES_BUTTON = (By.CSS_SELECTOR, ".color-bg-default > nav > a:nth-child(2)")
    NEW_REPOSITORY_BUTTON = (By.CSS_SELECTOR, ".color-border-muted.py-3 > a")


class RepositoryPageLocators:
    REPOSITORY_NAME = (By.CSS_SELECTOR, "strong > a")
    SETTINGS_BUTTON = (By.CSS_SELECTOR, "#settings-tab > span:nth-child(2)")
    QUICK_SETUP_MESSAGE = (By.CSS_SELECTOR, "div.Box-header")


class RepositorySettingsPageLocators:
    DELETE_REPOSITORY_BUTTON = (By.CSS_SELECTOR, "li:nth-child(4) > details > summary")
    PLEASE_TYPE_MESSAGE = (
        By.CSS_SELECTOR,
        "div.Box-body.overflow-auto > p:nth-child(1) > strong:nth-child(2)"
    )
    INPUT_FIELD = (By.CSS_SELECTOR, "div.Box-body.overflow-auto > form > p > input")
    I_UNDERSTAND_BUTTON = (By.CSS_SELECTOR, "div.Box-body.overflow-auto > form > button")
    RENAME_REPOSITORY_FIELD = (By.CSS_SELECTOR, "#rename-field")
    RENAME_BUTTON = (By.CSS_SELECTOR, "form.d-flex > button")



