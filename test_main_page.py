from selenium.webdriver.common.by import By


LINK = "http://selenium1py.pythonanywhere.com/"


def go_to_login_page(browser):
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()


def test_guest_can_go_to_login_page(browser):
    browser.get(LINK)
    go_to_login_page(browser)
