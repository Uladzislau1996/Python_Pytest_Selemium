from .base_page import BasePage 
from .locators import AddToBasketLocators

class BasketPage(BasePage):
    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*AddToBasketLocators.CHECK_FOR_EMPTY_BASKET), \
            "Basket isn't empty!"

    def should_be_text_that_basket_is_empty(self):
        assert self.is_element_present(*AddToBasketLocators.CHECK_EMPTY_BASKET_TEXT), \
            "Not text that basket is empty"

