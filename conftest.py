import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions



def pytest_addoption(parser)->None:
    parser.addoption(
        '--browser_name', action='store', default='chrome',
        help='Choose browser: chrome or firefox'
    )
    parser.addoption(
        '--language', action='store', default='en',
        help='Choose language'
    )


@pytest.fixture
def browser(request):
    language = request.config.getoption('language')
    browser_name = request.config.getoption('browser_name')

    if browser_name == 'chrome':
        print("\nstart chrome browser for test..")
        options_chrome = ChromeOptions()
        options_chrome.add_experimental_option(
            'prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options_chrome)
    elif browser_name == 'firefox':
        print("\nstart firefox browser for test..")
        options_firefox = FirefoxOptions()
        options_firefox.set_preference('intl.accept_languages', language)
        browser = webdriver.Firefox(options=options_firefox)
    else:
        raise ValueError("Browser name must be 'chrome' or 'firefox'")
    browser.implicitly_wait(5)
    yield browser
    print("\nstop chrome browser for test..")
    browser.quit()
