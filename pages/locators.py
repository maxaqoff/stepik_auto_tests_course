from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, 'span.btn-group')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, '#content_inner>p')
    ITEMS_IN_BASKET = (By.CSS_SELECTOR, '.col-sm-6.h3')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    PASSWORD = (By.CSS_SELECTOR, '#id_registration-password1')
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, '.btn.btn-lg.btn-primary[name="registration_submit"]')


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class ProductPageLocators:
    BASKET_FORM = (By.CSS_SELECTOR, "#add_to_basket_form")
    CURR_PRODUCT_NAME = (By.CSS_SELECTOR, "div>h1")
    CURR_PRODUCT_PRICE = (By.CSS_SELECTOR, 'div.col-sm-6.product_main>p.price_color')
    ADDED_PRODUCT_NAME = (By.CSS_SELECTOR, "div.alertinner>strong")
    ADDED_BASKET_PRICE = (By.CSS_SELECTOR, 'div.alertinner>p>strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert.alert-safe.alert-noicon.alert-success.fade.in')
