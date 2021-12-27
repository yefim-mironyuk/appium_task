# CHANGE PATH VARIABLE ACCORDING TO APK FILE LOCATION
path = ""


class DesiredCapabilities:
    tasksAppCapabilities = {
        "appium:deviceName": "Android Emulator",
        "platformName": "Android",
        "appium:app": path,
    }

    webCapabilities = {
        "appium:deviceName": "Android Emulator",
        "platformName": "Android",
        "browserName": "chrome"
    }
