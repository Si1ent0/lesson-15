import pytest
from selene import browser

@pytest.fixture(params=['desktop', 'mobile'])
def browser_setup(request):
    if request.param == 'desktop':
        browser.config.window_width = 1920
        browser.config.window_height = 1080

    if request.param == 'mobile':
        browser.config.window_width = 375
        browser.config.window_height = 667
    yield
    browser.quit()


@pytest.fixture
def desktop_setup():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield
    browser.quit()


@pytest.fixture
def mobile_setup():
    browser.config.window_width = 375
    browser.config.window_height = 667
    yield
    browser.quit()


@pytest.fixture(params=[(1920, 1080, 'desktop'), (375, 667, 'mobile')])
def browser_setup_window(request):
    if request.param[2] == 'desktop':
        browser.config.window_width = request.param[0]
        browser.config.window_height = request.param[1]
        return request.param[2]

    if request.param[2] == 'mobile':
        browser.config.window_width = request.param[0]
        browser.config.window_height = request.param[1]
        return request.param[2]
