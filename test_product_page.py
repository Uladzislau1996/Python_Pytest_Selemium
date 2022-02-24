import pytest
from .pages.basket_page import BasketPage
from .pages.base_page import BasePage
from .pages.main_page import MainPage
from .pages.product_page import ProductPage

#@pytest.mark.parametrize('link', ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail),"8", "9"])
#def test_guest_can_add_product_to_basket(browser, link):
    #link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    #page = MainPage(browser, link)
    #page.open()
    #page = ProductPage(browser, link)
    #page.add_to_basket()
    #page.solve_quiz_and_get_code()
    #page.should_be_correct_name_and_cost_of_book()

#def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    #page = MainPage(browser, link)
    #page.open()
    #page = ProductPage(browser, link)
    #page.add_to_basket()
    #page.should_not_be_success_message()

#def test_guest_cant_see_success_message(browser):
    #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    #page = MainPage(browser, link)
    #page.open()
    #page = ProductPage(browser, link)
    #page.should_not_be_success_message()

#def test_message_disappeared_after_adding_product_to_basket(browser):
    #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    #page = MainPage(browser, link)
    #page.open()
    #page = ProductPage(browser, link)
    #page.add_to_basket()
    #page.should_be_disappeared_message()

#def test_guest_should_see_login_link_on_product_page(browser):
    #link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    #page = BasePage(browser, link)
    #page.open()
    #page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasePage(browser, link)
    page.open()
    page.go_to_basket_page()
    page = BasketPage(browser, link)
    page.should_not_be_product_in_basket()
    page.should_be_text_that_basket_is_empty()