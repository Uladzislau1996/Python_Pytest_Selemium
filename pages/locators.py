from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class AddToBasketLocators():
    BOOKS_NAME = (By.CSS_SELECTOR, ".product_main>h1")
    BOOKS_COST = (By.CSS_SELECTOR, ".product_main>.price_color")
    BOOKS_NAME_CHECK = (By.CSS_SELECTOR, ".alertinner>strong")
    BOOKS_COST_CHECK = (By.CSS_SELECTOR, ".alertinner>p>strong")
 