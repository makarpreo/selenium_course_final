import math

from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators

class MainPage(BasePage):
    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
        # return LoginPage(browser=self.browser, url=self.browser.current_url)

    def should_be_login_link(self, args=MainPageLocators.LOGIN_LINK):
        assert self.is_element_present(*args), "Login link is not presented"

    def guest_can_go_to_basket_and_busket_empty(self):
        link = self.browser.find_element(*MainPageLocators.BASKET_LINK)
        link.click()
        assert self.is_element_present(*MainPageLocators.BASKET_EMPTY_TEXT), 'basket isnt empty'

    def add_to_basket(self):
        self.browser.find_element(*MainPageLocators.BASKET_LINK).click()  # добавить в корзину
    #
    # def solve_quiz_and_get_code(self):  # расчет
    #     alert = self.browser.switch_to.alert
    #     x = alert.text.split(" ")[2]
    #     answer = str(math.log(abs((12 * math.sin(float(x))))))
    #     alert.send_keys(answer)
    #     alert.accept()
    #     try:
    #         alert = self.browser.switch_to.alert
    #         alert_text = alert.text
    #         print(f"Your code: {alert_text}")
    #         alert.accept()
    #     except NoAlertPresentException:
    #         print("No second alert presented")

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer "
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина

