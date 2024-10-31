import math
from typing import Any

from selenium.common.exceptions import (NoSuchElementException,
                                        TimeoutException,
                                        NoAlertPresentException)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .locators import BasePageLocators


class BasePage:
    """Базовая страница для проекта"""

    def __init__(self, browser: Any, url: str, timeout: int = 10) -> None:
        """
        Конструктор класса
        :param browser: браузер
        :param url: адрес страницы
        :param timeout: время задержки для неявного ожидания
        """
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self) -> None:
        """Метод открывает нужную страницу"""
        self.browser.get(self.url)

    def is_element_present(self, how: str, what: str) -> bool:
        """
        Метод проверяет наличие элемента на странице
        :param how: метод поиска элемента
        :param what: селектор элемента
        :return: True - элемент есть на странице, False - элемент отсутствует
        """
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(
            self, how: str, what: str,
            timeout: int = 4) -> bool:
        """
        Метод проверяет, что элемент не появляется на странице
        :param how: метод поиска элемента
        :param what: селектор элемента
        :param timeout: время задержки для явного ожидания
        :return: False - элемент есть на странице, True - элемент отсутствует
        """
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_displayed(self, how: str, what: str, timeout: int = 4) -> bool:
        """
        Метод проверяет, что элемент исчезает со страницы
        :param how: метод поиска элемента
        :param what: селектор элемента
        :param timeout: время задержки для явного ожидания
        :return: True - элемент появился на странице,
        False - элемент не появился
        """
        try:
            (WebDriverWait(self.browser, timeout, 1, [TimeoutException]).
             until_not(EC.presence_of_element_located((how, what))))
        except TimeoutException:
            return False
        return True

    def click_on_element(self, how: str, what: str) -> None:
        """
        Метод нажимает на найденный элемент
        :param how: метод поиска элемента
        :param what: селектор элемента
        :return: None
        """
        self.browser.find_element(how, what).click()

    def insert_in_field(self, how: str, what: str, data: str) -> None:
        """
        Метод осуществляет ввод данных в поле
        :param how: метод поиска элемента
        :param what: селектор элемента
        :param data: вводимые данные
        :return: None
        """
        self.browser.find_element(how, what).send_keys(data)

    def get_text_element(self, how: str, what: str) -> str:
        """
        Метод возвращает текст отображаемый элементом
        :param how: метод поиска элемента
        :param what: селектор элемента
        :return: текст отображаемый элементом
        """
        return self.browser.find_element(how, what).text

    def go_to_login_page(self) -> None:
        """
        Метод осуществляет переход на страницу авторизации и регистрации
        :return: None
        """
        self.click_on_element(*BasePageLocators.LOGIN_LINK)

    def go_to_basket(self) -> None:
        """
        Метод осуществляет переход на страницу корзины покупок
        :return: None
        """
        self.click_on_element(*BasePageLocators.BASKET_LINK)

    def should_be_login_link(self) -> None:
        """
        Метод проверяет наличие ссылки на страницу авторизации и регистрации
        :return: None
        """
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), \
            "Login link is not presented."

    def solve_quiz_and_get_code(self) -> None:
        """
        Метод вводит капчу (считает значение answer с учетом x
        полученным из alert)
        :return: None
        """
        alert: Any = self.browser.switch_to.alert
        x: str = alert.text.split(" ")[2]
        answer: str = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert: Any = self.browser.switch_to.alert
            alert_text: str = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_be_authorized_user(self) -> None:
        """
        Метод проверяет авторизован ли пользователь
        :return: None
        """
        assert self.is_element_present(*BasePageLocators.USER_ICON), \
            "User icon is not presented, probably unauthorised user"
