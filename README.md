# This repository contains example of Appium testing framework


# How to install it


1) Clone the repository.

``$ git clone https://github.com/yefim-mironyuk/appium_task.git``

2) Install allure command line and add the allure folder installation into system environment variable: https://docs.qameta.io/allure/#_installing_a_commandline

3) Install pipenv for creation virtual environment and installation packages: https://pipenv.pypa.io/en/latest/  

``$ pip install --user pipenv``

4) Install dependencies:

``pipenv install``

**Requirements**

You need:

1) Appium server and Android Studio be installed on your system. 

2) Create device emulator in Android Studio. This framework using `Pixel 2` emulator on `Android 7.1.1`

You can configure ``desired_capabilities.py`` file according to your emulator, also you need to change ``path`` variable according to apk file location.

EX: ``C:\\Users\\Yaukhim.Miraniuk\\Desktop\\app1.apk``


# How to run it


Use: `` python -m pytest .\tests\test_mobile_web\ `` to run mobile web tests.

Use: `` python -m pytest .\tests\test_native_app\ `` to run native app tests.


**Parameters**



``--alluredir=report_allure/`` to create Allure report.


**Allure report**

Use: ``allure serve report_allure`` to open Allure report.

**Logging**

Logs are in ``debug.log``
