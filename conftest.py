import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from typing import Any


def pytest_addoption(parser: Any) -> None:
    """
    Функция добавляет опции к запуску pytest
    :param parser: Any
    :return: None
    """
    parser.addoption(
        '--browser_name', action='store', default='chrome',
        help='Choose browser: chrome or firefox'
    )
    parser.addoption(
        '--language', action='store', default='en',
        help='Choose language'
    )


@pytest.fixture
def browser(request: Any) -> Any:
    """
    Фикстура открывает и закрывает браузер
    :param request: запрос
    :return: Any
    """
    language: Any = request.config.getoption('language')
    browser_name: Any = request.config.getoption('browser_name')

    if browser_name == 'chrome':
        print("\nstart chrome browser for test..")
        options_chrome: ChromeOptions = ChromeOptions()
        options_chrome.add_experimental_option(
            'prefs', {'intl.accept_languages': language})
        browser: Any = webdriver.Chrome(options=options_chrome)
    elif browser_name == 'firefox':
        print("\nstart firefox browser for test..")
        options_firefox: FirefoxOptions = FirefoxOptions()
        options_firefox.set_preference('intl.accept_languages', language)
        browser: Any = webdriver.Firefox(options=options_firefox)
    else:
        raise ValueError("Browser name must be 'chrome' or 'firefox'")
    browser.implicitly_wait(5)
    yield browser
    print("\nstop chrome browser for test..")
    browser.quit()
