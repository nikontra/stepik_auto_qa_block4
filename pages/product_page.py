from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    """Класс содержит методы, которые относятся к странице товара"""

    def add_to_basket(self) -> None:
        """
        Метод осуществляет переход на страницу корины покупок
        из страницы товара
        :return: None
        """
        self.click_on_element(*ProductPageLocators.BASKET)
        try:
            WebDriverWait(self.browser, 2).until(
                EC.alert_is_present(), 'Timed out waiting for alert')
            self.solve_quiz_and_get_code()
        except TimeoutException:
            print("no alert")
        self.shout_be_message_success_added_to_basket()
        self.shout_be_price_basket()

    def shout_be_message_success_added_to_basket(self) -> None:
        """
        Метод проверяет появление сообщения об успешном добавлении
        товара в корзину
        :return: None
        """
        product_name: str = self.get_text_element(
            *ProductPageLocators.PRODUCT_NAME)
        message_success: str = self.get_text_element(
            *ProductPageLocators.MESSAGE_SUCCESS_ADDED_TO_BASKET)
        assert product_name == message_success, \
            "No message about adding an item to the cart"

    def shout_be_price_basket(self) -> None:
        """
        Метод проверяет соответствие стоимости корзины стоимости товара
        :return: None
        """
        product_price: str = self.get_text_element(
            *ProductPageLocators.PRODUCT_PRICE)
        message_price: str = self.get_text_element(
            *ProductPageLocators.MESSAGE_PRICE_BASKET)
        assert product_price == message_price, "Product price does not match"

    def should_not_be_success_message(self) -> None:
        """
        Метод проверяет, что сообщение об успешном добавлении товара
        в корзину отсутствует
        :return: None
        """
        assert self.is_not_element_present(
            *ProductPageLocators.MESSAGE_SUCCESS_ADDED_TO_BASKET), \
            "Success message is presented, but should not be"

    def should_disappeared_success_message(self) -> None:
        """
        Метод проверяет, что сообщение об успешном добавлении товара
        в корзину исчезает
        :return: None
        """
        assert self.is_displayed(
            *ProductPageLocators.MESSAGE_SUCCESS_ADDED_TO_BASKET), \
            "Success message is present"
