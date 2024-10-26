from selenium.webdriver.common.by import By


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    LOGIN_REGISTRATION = (By.CSS_SELECTOR, '#id_registration-email')
    PASSWORD_REGISTRATION = (By.CSS_SELECTOR, '#id_registration-password1')
    PASSWORD_CONFIRM = (By.CSS_SELECTOR, '#id_registration-password2')
    BUTTON_REGISTRATION = (By.CSS_SELECTOR, '.register_form .btn')


class ProductPageLocators:
    BASKET = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    MESSAGE_SUCCESS_ADDED_TO_BASKET = (By.CSS_SELECTOR, 'div.alert:nth-child(1) strong')
    MESSAGE_PRICE_BASKET = (By.CSS_SELECTOR, 'div.alert:nth-child(3) strong')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'div#content_inner h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'div#content_inner p.price_color')


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')
    BASKET_LINK = (By.CSS_SELECTOR, 'div.basket-mini a.btn')
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')

class BasketPageLocators:
    BASKET_MESSAGE = (By.CSS_SELECTOR, 'div.page_inner div.content p')
    BASKET_ITEMS = (By.CSS_SELECTOR, 'div.basket-items')