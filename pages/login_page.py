from .base_page import BasePage
from .locators import LoginPageLocators
from .main_page import MainPage

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # url = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer "
        # assert requests.head(url, allow_redirects=True) == 200
        assert "login" in self.url, 'login is not in url' # сообщение об ошибке

    def should_be_login_form(self):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = MainPage(self.browser, link)
        page.open()
        page.should_be_login_link(LoginPageLocators.REGISTRATION_FORM)

    def should_be_register_form(self):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = MainPage(self.browser, link)
        page.open()
        page.should_be_login_link(LoginPageLocators.LOGIN_FORM)

    def register_new_user(self, email, password):
        input1 = self.browser.find_element(*LoginPageLocators.REGISTRATION_pole1)
        input2 = self.browser.find_element(*LoginPageLocators.REGISTRATION_pole2)
        input3 = self.browser.find_element(*LoginPageLocators.REGISTRATION_pole3)
        input1.send_keys(email)
        input2.send_keys(password)
        input3.send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_FORM).click()







