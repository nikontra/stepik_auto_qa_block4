from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_login_page(self):
        self.should_be_basket_url()
        self.should_be_basket_empty()
        self.should_be_message_basket_empty()

    def should_be_basket_url(self):
        assert "basket" in self.browser.current_url, "Basket not in URL"

    def should_be_basket_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS),\
            "Basket is not empty"

    def should_be_message_basket_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_MESSAGE),\
            "Message empty basket missing"
