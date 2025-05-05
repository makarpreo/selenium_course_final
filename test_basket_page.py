from .pages.basket_page import BasketPage
from .pages.main_page import MainPage

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.basket_is_empty_positive()
    basket_page.basket_is_empty_niggative()


