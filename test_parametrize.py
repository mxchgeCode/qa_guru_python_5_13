import pytest
from selenium import webdriver
from selene import browser
"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""


@pytest.fixture(params=[(1920, 1080), (320, 240), (2560, 1440), (240, 320)])
def web_browser(request):
    chrome_options = webdriver.ChromeOptions()
    browser.config.driver_options = chrome_options
    browser.config.window_height = request.param[0]
    browser.config.window_width = request.param[1]
    yield browser
    browser.quit()


@pytest.mark.parametrize('web_browser', [(1920, 1080), (2560, 1440),], indirect=True)
def test_github_desktop(web_browser):
    web_browser.open('https://github.com/')
    web_browser.element('a.HeaderMenu-link--sign-in').click()


@pytest.mark.parametrize('web_browser', [(320, 240), (240, 320)], indirect=True)
def test_github_mobile(web_browser):
    browser.open('https://github.com/')
    browser.element('.flex-column [aria-label="Toggle navigation"]').click()
    browser.element('a.HeaderMenu-link--sign-in').click()
