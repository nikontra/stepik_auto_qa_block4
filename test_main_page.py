from typing import Any

import pytest

from .pages.main_page import MainPage
from .pages.login_page import LoginPage


LINK: str = "http://selenium1py.pythonanywhere.com/"


@pytest.mark.login_guest
class TestLoginFromMainPage:
    """Класс содержит тесты главной страница проекта"""

    def test_guest_can_go_to_login_page(self, browser: Any) -> None:
        """
        Метод тестирует переход на страницу авторизации и регистрации
        с главной страницы проекта
        :param browser: браузер
        :return: None
        """
        page: MainPage = MainPage(browser, LINK)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser: Any) -> None:
        """
        Метод тестирует наличие ссылки на страницу авторизации и регистрации
        на главной странице проекта
        :param browser: браузер
        :return: None
        """
        page: MainPage = MainPage(browser, LINK)
        page.open()
        page.should_be_login_link()
