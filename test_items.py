import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestLogin:
    def test_authorization(self, browser):
        browser.implicitly_wait(5)
        browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
        assert browser.find_element(By.CSS_SELECTOR, '#add_to_basket_form > button') is not None, 'элемент не найден'

#'#add_to_basket_form > button'