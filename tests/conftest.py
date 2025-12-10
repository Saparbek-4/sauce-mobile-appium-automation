import pytest
import allure
from allure_commons.types import AttachmentType
from drivers.driver_factory import get_driver
from pages.login_page import LoginPage
from utils.logger import logger

@pytest.hookimpl(hookwrapper=True, trylast=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    # store only call-step → does NOT break Allure
    if rep.when == "call":
        item.rep_call = rep


# ---------- DRIVER FIXTURE ----------
@pytest.fixture(scope="function")
def driver(request):
    env = request.config.getoption("--env")
    driver = get_driver(env)

    yield driver

    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        logger.error("Test failed — attaching screenshot")
        allure.attach(
            driver.get_screenshot_as_png(),
            name="Screenshot Failure",
            attachment_type=AttachmentType.PNG
        )

        try:
            logs = driver.get_log("logcat")
            allure.attach(
                "\n".join([str(l) for l in logs]),
                name="Logcat",
                attachment_type=AttachmentType.TEXT
            )
        except:
            pass

    driver.quit()


# ---------- PRODUCTS FIXTURE ----------
@pytest.fixture
def products_page(driver):
    login = LoginPage(driver)
    products_page = login.login("standard_user", "secret_sauce")
    assert products_page.is_loaded()
    return products_page



def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="local")
