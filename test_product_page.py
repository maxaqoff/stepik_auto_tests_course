from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.base_page import BasePage
import time
import pytest
#tests in this script check page with selected product

@pytest.mark.parametrize('page_num', (str(i) if i != 7 else pytest.param("bugged page_num", marks=pytest.mark.xfail)
                                      for i in range(0, 9)))
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, page_num):
    link = f"http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer{page_num}"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.compare_product_name()
    page.compare_price()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = f"http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = f"http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = f"http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_be_desapear()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.check_empty_basket_text()
    basket_page.should_not_be_products()


@pytest.mark.register_user
class TestUserAddToBasketFromProductPage:
    @staticmethod
    @pytest.fixture(scope="function", autouse=True)
    def setup(browser):
        link = r'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
        login_page = LoginPage(browser, link)
        login_page.open()
        login_page.register_new_user(str(time.time()) + "@fakemail.org", 'Pa$$w0rd123')
        BasePage.should_be_authorized_user(login_page)

    @staticmethod
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(browser):
        link = f"http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.compare_product_name()
        page.compare_price()

    @staticmethod
    def test_user_cant_see_success_message(browser):
        link = f"http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()
