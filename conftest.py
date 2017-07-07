import pytest
from browser import get_driver


def pytest_exception_interact(node, call, report):
    get_driver().save_screenshot("error.png")


@pytest.fixture(scope="module")
def driver():
    return get_driver()