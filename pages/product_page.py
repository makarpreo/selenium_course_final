from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators


class ProductPage(BasePage):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer "
    def test_guest_can_go_to_login_page_from_product_page(self):
        link = self.browser.find_element(*ProductPageLocators.LOGIN_LINK)
        link.click()
        assert self.is_element_present(*ProductPageLocators.LOGIN_CHECK)

    def should_be_login_link(self, args=ProductPageLocators.LOGIN_LINK):
        assert self.is_element_present(*args), "Login link is not presented"

    def basket(self):
        link = self.browser.find_element(*ProductPageLocators.BASKET_LINK)
        link.click()
        assert self.is_element_present(*ProductPageLocators.BASKET_EMPTY_TEXT), 'basket isnt empty'



