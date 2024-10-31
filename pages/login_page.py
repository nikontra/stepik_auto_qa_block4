from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    """Класс содержащий методы, которые относятся к корзине покупок"""

    def register_new_user(self, email: str, password: str) -> None:
        """
        Метод регистрирует нового пользователя
        :param email: адрес электронной почты
        :param password: пароль
        :return: None
        """
        self.insert_in_field(
            *LoginPageLocators.LOGIN_REGISTRATION, email
        )
        self.insert_in_field(
            *LoginPageLocators.PASSWORD_REGISTRATION, password
        )
        self.insert_in_field(
            *LoginPageLocators.PASSWORD_CONFIRM, password
        )
        self.click_on_element(
            *LoginPageLocators.BUTTON_REGISTRATION
        )

    def should_be_login_page(self) -> None:
        """
        Метод проверяет корректность отображения страницы
        авторизации и регистрации
        :return: None
        """
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self) -> None:
        """
        Метод проверяет наличие в URL слова "login"
        :return: None
        """
        assert "login" in self.browser.current_url, "Login not in URL"

    def should_be_login_form(self) -> None:
        """
        Метод проверяет наличие формы авторизации
        :return: None
        """
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            "Login form is not present."

    def should_be_register_form(self) -> None:
        """
        Метод проверяет наличие формы регистрации
        :return: None
        """
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), \
            "Register form is not present."
