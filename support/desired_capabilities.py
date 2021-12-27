from .config import CapsConstants


class DesiredCapabilities:
    mobileCapabilities = {
        "appium:deviceName": CapsConstants.device_name,
        "platformName": CapsConstants.platform_name,
        "appium:app": CapsConstants.path,
    }

    webCapabilities = {
        "appium:deviceName": CapsConstants.device_name,
        "platformName": CapsConstants.platform_name,
        "browserName": CapsConstants.browser_name,
    }
