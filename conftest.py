import pytest
from selene.support.shared import browser


@pytest.fixture()
def browser_open_and_maximize_window():
    browser.open('https://www.google.com/')
    browser.driver.maximize_window()
