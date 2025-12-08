import pytest
from drivers.driver_factory import get_driver

@pytest.fixture(scope='function')
def driver(request):
    platform = request.config.getoption('--platform') or 'android'
    driver = get_driver(platform=platform)
    yield driver
    try:
        driver.quit()
    except Exception:
        pass

def pytest_addoption(parser):
    parser.addoption('--platform', action='store', default='android', help='platform to run tests')
