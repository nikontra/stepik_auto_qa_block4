from typing import Tuple

from selenium.webdriver.common.by import By


class MainPageLocators:
    pass


class LoginPageLocators:
    """
    Класс содержит локаторы относящиеся к странице авторизации и регистрации
    """
    LOGIN_FORM: Tuple[str, str] = (
        By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM: Tuple[str, str] = (
        By.CSS_SELECTOR, '#register_form')
    LOGIN_REGISTRATION: Tuple[str, str] = (
        By.CSS_SELECTOR, '#id_registration-email')
    PASSWORD_REGISTRATION: Tuple[str, str] = (
        By.CSS_SELECTOR, '#id_registration-password1')
    PASSWORD_CONFIRM: Tuple[str, str] = (
        By.CSS_SELECTOR, '#id_registration-password2')
    BUTTON_REGISTRATION: Tuple[str, str] = (
        By.CSS_SELECTOR, '.register_form .btn')


class ProductPageLocators:
    """
    Класс содержит локаторы относящиеся к странице товара
    """
    BASKET: Tuple[str, str] = (
        By.CSS_SELECTOR, 'button.btn-add-to-basket')
    MESSAGE_SUCCESS_ADDED_TO_BASKET: Tuple[str, str] = (
        By.CSS_SELECTOR, 'div.alert:nth-child(1) strong')
    MESSAGE_PRICE_BASKET: Tuple[str, str] = (
        By.CSS_SELECTOR, 'div.alert:nth-child(3) strong')
    PRODUCT_NAME: Tuple[str, str] = (
        By.CSS_SELECTOR, 'div#content_inner h1')
    PRODUCT_PRICE: Tuple[str, str] = (
        By.CSS_SELECTOR, 'div#content_inner p.price_color')


class BasePageLocators:
    """
    Класс содержит локаторы относящиеся к базовой странице проекта
    """
    LOGIN_LINK: Tuple[str, str] = (
        By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID: Tuple[str, str] = (
        By.CSS_SELECTOR, '#login_link_inc')
    BASKET_LINK: Tuple[str, str] = (
        By.CSS_SELECTOR, 'div.basket-mini a.btn')
    USER_ICON: Tuple[str, str] = (
        By.CSS_SELECTOR, '.icon-user')


class BasketPageLocators:
    """
    Класс содержит локаторы относящиеся к странице корзины покупок
    """
    BASKET_MESSAGE: Tuple[str, str] = (
        By.CSS_SELECTOR, 'div.page_inner div.content p')
    BASKET_ITEMS: Tuple[str, str] = (
        By.CSS_SELECTOR, 'div.basket-items')
