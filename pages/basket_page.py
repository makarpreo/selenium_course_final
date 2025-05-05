from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators


class BasketPage(BasePage):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer "

    def should_be_login_link(self, args=ProductPageLocators.LOGIN_LINK):
        assert self.is_element_present(*args), "Login link is not presented"

    def basket_is_empty_positive(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_EMPTY_TEXT), 'basket isnt empty'

    def basket_is_empty_niggative(self):
        assert not(self.is_not_element_present(*ProductPageLocators.BASKET_EMPTY_TEXT)), 'basket shouldnt be empty, but its not'



