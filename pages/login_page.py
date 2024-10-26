from .base_page import BasePage
from .locators import LoginPageLocators, BasePageLocators


class LoginPage(BasePage):

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.LOGIN_REGISTRATION)
        email_input.send_keys(email)
        password_input = self.browser.find_element(*LoginPageLocators.PASSWORD_REGISTRATION)
        password_input.send_keys(password)
        confirm_input = self.browser.find_element(*LoginPageLocators.PASSWORD_CONFIRM)
        confirm_input.send_keys(password)
        button_register = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTRATION)
        button_register.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Login not in URL"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not present."

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not present."