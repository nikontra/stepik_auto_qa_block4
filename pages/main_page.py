from typing import Any

from .base_page import BasePage


class MainPage(BasePage):
    """Класс содержит методы, которые относятся к главной странице проекта"""
    def __init__(self, *args: tuple[Any,]) -> None:
        """
        Конструктор класса
        :param args:
        """
        super().__init__(*args)
