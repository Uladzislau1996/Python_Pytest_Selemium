from .base_page import BasePage
from .locators import AddToBasketLocators
from .locators import MainPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math

class PageObject(BasePage):
    def should_be_correct_name_and_cost_of_book(self):
        self.should_be_correct_name_of_product()
        self.should_be_correct_cost_of_product()
    
    def should_be_correct_name_of_product(self):
        books_name = self.browser.find_element(*AddToBasketLocators.BOOKS_NAME)
        books_name_check = self.browser.find_element(*AddToBasketLocators.BOOKS_NAME_CHECK)
        assert books_name.text == books_name_check.text, "Bug in the name of product"
    
    def should_be_correct_cost_of_product(self):
        books_cost = self.browser.find_element(*AddToBasketLocators.BOOKS_COST)
        books_cost_check = self.browser.find_element(*AddToBasketLocators.BOOKS_COST_CHECK)
        assert books_cost.text == books_cost_check.text, "Bug in the cost of product"

    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*MainPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

