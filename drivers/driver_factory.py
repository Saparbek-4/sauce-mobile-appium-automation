from drivers.android_driver import create_android_driver
from drivers.browserstack_driver import create_browserstack_driver

def get_driver(env="local"):
    if env == "local":
        return create_android_driver("config/dev.yml")
    elif env == "browserstack":
        return create_browserstack_driver("config/browserstack.yml")
    else:
        raise ValueError("Unknown driver environment")