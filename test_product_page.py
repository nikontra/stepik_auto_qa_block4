from typing import Any, Tuple

import pytest
import time

from .pages.login_page import LoginPage
from .pages.main_page import MainPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage


LINK_MAIN: str = "http://selenium1py.pythonanywhere.com/"
LINK_PRODUCT: str = ("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
LINK_REGISTRATION: str = "http://selenium1py.pythonanywhere.com/accounts/login/"


def get_email_password() -> Tuple[str, str]:
    """
    Функция создает пару из электронной почты и пароля
    :return: Tuple[str, str]
    """
    return str(time.time()) + "@fakemail.org", str(time.time())


def test_guest_cant_see_success_message(browser: Any) -> None:
    """
    Функция проверяет отсутствие сообщения об успешном добавлении
    товара в корзину для гостя
    :param browser:
    :return: None
    """
    page: ProductPage = ProductPage(browser, LINK_PRODUCT, 0)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.need_review
@pytest.mark.parametrize('link', [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
    pytest.param(
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
        marks=pytest.mark.xfail),
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
])
def test_guest_can_add_product_to_basket(
        browser: Any, link: list[str]) -> None:
    """
    Функция проверяет, может ли гость добавить товар в корзину
    :param browser: браузер
    :param link: список ссылок на товар с различными предложениями
    :return: None
    """
    page: ProductPage = ProductPage(browser, link)
    page.open()
    page.add_to_basket()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(
        browser: Any) -> None:
    """
    Функция проверяет отсутствие сообщения об успехе после добавления гостем
    товара в корзину покупок
    :param browser: браузер
    :return: None
    """
    page: ProductPage = ProductPage(browser, LINK_PRODUCT, 0)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(
        browser: Any) -> None:
    """
    Функция проверяет исчезновение сообщения об успехе после
    добавления гостем товара в корзину покупок
    :param browser: браузер
    :return: None
    """
    page: ProductPage = ProductPage(browser, LINK_PRODUCT, 0)
    page.open()
    page.add_to_basket()
    page.should_disappeared_success_message()


def test_guest_should_see_login_link_on_product_page(browser: Any) -> None:
    """
    Функция проверяет наличие ссылки на страницу авторизации и
    регистрации для гостя на странице товара
    :param browser: браузер
    :return: None
    """
    page: ProductPage = ProductPage(browser, LINK_PRODUCT)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser: Any) -> None:
    """
    Функция проверяет, может ли гость перейти на страницу
    авторизации и регистрации со страницы товара
    :param browser: браузер
    :return: None
    """
    page: ProductPage = ProductPage(browser, LINK_PRODUCT)
    page.open()
    page.go_to_login_page()
    login_page: LoginPage = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(
        browser: Any) -> None:
    """
    Функция проверяет, может ли гость перейти на страницу корзины покупок
    с главной страницы сайта
    :param browser: браузер
    :return: None
    """
    page: MainPage = MainPage(browser, LINK_MAIN)
    page.open()
    page.go_to_basket()
    basket_page: BasketPage = BasketPage(browser, browser.current_url, 0)
    basket_page.should_be_basket_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(
        browser: Any) -> None:
    """
    Функция проверяет, может ли гость перейти на страницу корзины покупок
    со страницы товара
    :param browser: браузер
    :return: None
    """
    page: ProductPage = ProductPage(browser, LINK_PRODUCT)
    page.open()
    page.go_to_basket()
    basket_page: BasketPage = BasketPage(browser, browser.current_url, 0)
    basket_page.should_be_basket_page()


class TestUserAddToBasketFromProductPage:
    """Класс содержащий методы тестирования авторизованного пользователя"""

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser: Any) -> None:
        """
        Фикстура регистрирует нового пользователя
        :param browser:
        :return: None
        """
        page: LoginPage = LoginPage(browser, LINK_REGISTRATION)
        page.open()
        page.register_new_user(*get_email_password())
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser: Any) -> None:
        """
        Метод проверяет отображение сообщения об успешном добавлении товара
        в корзину для авторизованного пользователя
        :param browser: браузер
        :return: None
        """
        page: ProductPage = ProductPage(browser, LINK_PRODUCT, 0)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser: Any) -> None:
        """
        Метод проверяет, может ли добавить товар в корзину
        авторизованный пользователь
        :param browser: браузер
        :return: None
        """
        page: ProductPage = ProductPage(browser, LINK_PRODUCT, 0)
        page.open()
        page.add_to_basket()
