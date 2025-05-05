import time
import pytest
from selenium.webdriver.common.by import By
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
import time
# def test_guest_can_go_to_login_page(browser):
#     link = "http://selenium1py.pythonanywhere.com"
#     page = MainPage(browser, link)
#     page.open()
#     page.go_to_login_page()
#     time.sleep(2)
#     login_page = LoginPage(browser, browser.current_url)
#     login_page.should_be_login_page()


# def test_guest_can_go_to_login_page(browser):
#     link = "http://selenium1py.pythonanywhere.com"
#     page = MainPage(browser, link)
#     page.open()
#     login_page = page.go_to_login_page()
#     login_page.should_be_login_page()

# def test_all_login_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
#     page = LoginPage(browser, link)
#     page.should_be_login_page()

# def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
#     link = 'http://selenium1py.pythonanywhere.com/ru/'
#     page = MainPage(browser, link)
#     page.open()
#     page.guest_can_go_to_basket_and_busket_empty()

@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/ru/'
        page = MainPage(browser, link)
        page.open()
        page.guest_can_go_to_basket_and_busket_empty()

    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        time.sleep(2)
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

