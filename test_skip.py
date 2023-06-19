import pytest
from selenium import webdriver
from selene import browser
"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""


@pytest.fixture(params=[(1920, 1080), (320, 240), (2560, 1440), (240, 320)],
                ids=['desktop', 'mobile', 'desktop', 'mobile'])
def web_browser(request):
    chrome_options = webdriver.ChromeOptions()
    browser.config.driver_options = chrome_options
    id = request.node.callspec.id
    browser.config.window_height = request.param[0]
    browser.config.window_width = request.param[1]
    yield browser, id
    browser.quit()


def test_github_desktop(web_browser):
    w_browser, id = web_browser
    if 'mobile' in id:
        pytest.skip('Для теста не подходит мобильное соотношение сторон')
    w_browser.open('https://github.com/')
    w_browser.element('a.HeaderMenu-link--sign-in').click()


def test_github_mobile(web_browser):
    w_browser, id = web_browser
    if 'desktop' in id:
        pytest.skip('Для теста не подходит десктопное соотношение сторон')
    w_browser.open('https://github.com/')
    w_browser.element('.flex-column [aria-label="Toggle navigation"]').click()
    w_browser.element('a.HeaderMenu-link--sign-in').click()

