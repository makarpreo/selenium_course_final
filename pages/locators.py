from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, '#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a')
    BASKET_EMPTY_TEXT = (By.CSS_SELECTOR, '#content_inner > p')

class LoginPageLocators():
    LOGIN_LINK = (By.ID, "registration_link")
    REGISTRATION_FORM = (By.CSS_SELECTOR, '#register_form > button')
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form > button')
    REGISTRATION_pole1 = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTRATION_pole2 = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTRATION_pole3 = (By.CSS_SELECTOR, '#id_registration-password2')

class BasePageLocators():
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, '#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a')

#http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/
class ProductPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_CHECK = (By.CSS_SELECTOR, '#login_form > h2')
    BASKET_LINK = (By.CSS_SELECTOR, '#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a')
    BASKET_EMPTY_TEXT = (By.CSS_SELECTOR, '#content_inner > p')

