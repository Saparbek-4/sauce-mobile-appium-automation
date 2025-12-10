import os
import yaml
from appium.webdriver import Remote
from appium.options.android import UiAutomator2Options

def create_browserstack_driver(config_path):
    with open(config_path, "r") as f:
        cfg = yaml.safe_load(f)

    user = os.getenv("BS_USERNAME")
    key = os.getenv("BS_ACCESS_KEY")

    caps = cfg["capabilities"]

    caps["app"] = os.getenv("BS_APP_ID")

    options = UiAutomator2Options()
    for k, v in caps.items():
        options.set_capability(k, v)

    url = f"http://{user}:{key}@hub.browserstack.com/wd/hub"

    return Remote(command_executor=url, options=options)
