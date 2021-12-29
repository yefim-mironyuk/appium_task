from appium.webdriver.common.appiumby import AppiumBy


class MainPageLocators:
    CREATE_NEW_TASK_BUTTON = (AppiumBy.ID, "com.Tasks.Tasks:id/addTaskButton")
    NEW_TASK_ON_MAIN_PAGE = (AppiumBy.XPATH, "//android.widget.ListView/android.widget.TextView[last()]")


class CreateTaskPageLocators:
    NEW_TASK_TITLE_FIELD = (AppiumBy.ID, "com.Tasks.Tasks:id/taskTitleEditText")
    NEW_TASK_DESCRIPTION_FIELD = (AppiumBy.ID, "com.Tasks.Tasks:id/taskDescriptionEditText")
    SAVE_NEW_TASK_BUTTON = (AppiumBy.ID, "com.Tasks.Tasks:id/saveTaskButton")


class TaskPageLocators:
    TITLE_FIELD = (AppiumBy.ID, "com.Tasks.Tasks:id/taskTitleEditText")
    SAVE_CHANGES_BUTTON = (AppiumBy.ID, "com.Tasks.Tasks:id/saveTaskButton")
    ERROR_MESSAGE = (AppiumBy.ID, "com.Tasks.Tasks:id/snackbar_text")
