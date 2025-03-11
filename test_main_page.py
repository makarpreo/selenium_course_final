from selenium.webdriver.common.by import By


def test_guest_should_see_login_link(browser):
    browser.get("http://selenium1py.pythonanywhere.com/")
    browser.find_element(By.CSS_SELECTOR, "#login_link")
