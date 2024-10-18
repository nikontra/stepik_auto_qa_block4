from .pages.main_page import MainPage
from selenium.webdriver.common.by import By


LINK = "http://selenium1py.pythonanywhere.com/"


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, LINK)
    page.open()
    page.go_to_login_page()
