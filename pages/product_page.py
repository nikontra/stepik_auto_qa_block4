from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def add_to_basket(self):
        basket = self.browser.find_element(*ProductPageLocators.BASKET)
        basket.click()
        # self.solve_quiz_and_get_code()
        self.shout_be_message_success_added_to_basket()
        self.shout_be_price_basket()

    def shout_be_message_success_added_to_basket(self):
        product_name = self.get_product_name()
        message_success = self.browser.find_element(
            *ProductPageLocators.MESSAGE_SUCCESS_ADDED_TO_BASKET).text
        assert product_name == message_success, "No message about adding an item to the cart"

    def shout_be_price_basket(self):
        product_price = self.get_product_price()
        message_price = self.browser.find_element(*ProductPageLocators.MESSAGE_PRICE_BASKET).text
        assert product_price == message_price, "Product price does not match"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_SUCCESS_ADDED_TO_BASKET),\
            "Success message is presented, but should not be"

    def should_disappeared_success_message(self):
        assert self.is_displayed(*ProductPageLocators.MESSAGE_SUCCESS_ADDED_TO_BASKET),\
            "Success message is present"
