from appium.webdriver import Remote
from appium.options.android import UiAutomator2Options
import yaml
import os

def create_android_driver(config_path='config/dev.yml'):
    with open(config_path, 'r') as f:
        cfg = yaml.safe_load(f)

    app_path = os.path.abspath(cfg['app']['apk_path'])

    options = UiAutomator2Options()

    options.set_capability("platformName", cfg['device']['platformName'])
    options.set_capability("platformVersion", cfg['device']['platformVersion'])
    options.set_capability("deviceName", cfg['device']['deviceName'])
    options.set_capability("app", app_path)
    options.set_capability("appWaitActivity", cfg['app']['activity'])
    options.set_capability("autoGrantPermissions", True)

    return Remote(
        command_executor='http://localhost:4723',
        options=options
    )
