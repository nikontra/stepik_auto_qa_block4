from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    """Класс содержащий методы, которые относятся к корзине покупок"""

    def should_be_basket_page(self) -> None:
        """
        Метод проверяет корректность отображения страницы корзины покупок
        :return: None
        """
        self.should_be_basket_url()
        self.should_be_basket_empty()
        self.should_be_message_basket_empty()

    def should_be_basket_url(self) -> None:
        """
        Метод проверяет наличие в URL слова "basket"
        :return: None
        """
        assert "basket" in self.browser.current_url, "Basket not in URL"

    def should_be_basket_empty(self) -> None:
        """
        Метод проверяет, что корзина покупок пуста
        :return: None
        """
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Basket is not empty"

    def should_be_message_basket_empty(self) -> None:
        """
        Метод проверяет наличие сообщения, что корзина покупок пуска
        :return: None
        """
        assert self.is_element_present(*BasketPageLocators.BASKET_MESSAGE), \
            "Message empty basket missing"
