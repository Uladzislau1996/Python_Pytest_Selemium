from selenium.webdriver.common.by import By


class MainPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    CONFIRM_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form>button")

class AddToBasketLocators():
    BOOKS_NAME = (By.CSS_SELECTOR, ".product_main>h1")
    BOOKS_COST = (By.CSS_SELECTOR, ".product_main>.price_color")
    BOOKS_NAME_CHECK = (By.CSS_SELECTOR, ".alertinner>strong")
    BOOKS_COST_CHECK = (By.CSS_SELECTOR, ".alertinner>p>strong")
    CHECK_FOR_EMPTY_BASKET = (By.CSS_SELECTOR, ".basket-title")
    CHECK_EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner>p")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    GO_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group>a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
 