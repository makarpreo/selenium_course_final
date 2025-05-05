import pytest

from .pages.login_page import LoginPage
from .pages.main_page import MainPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
import time # в начале файла


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/')
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = MainPage(browser, link)
    page.open()
    time.sleep(2)
    page.add_to_basket()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.basket_is_empty_positive()

class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        login_page = LoginPage(browser, 'http://selenium1py.pythonanywhere.com/ru/accounts/login/')
        login_page.open()
        login_page.register_new_user(str(time.time()) + "@fakemail.org", 'Axe126213')
        login_page.should_be_authorized_user()


    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
        page = MainPage(browser, link)
        page.open()
        page.add_to_basket()
        # # page.solve_quiz_and_get_code()





