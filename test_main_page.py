from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import PageObject
import time

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   
    page.open()                      
    page.go_to_login_page()      
    login_page = page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()   

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = MainPage(browser, link)
    page.open()
    page = PageObject(browser, link)
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_correct_name_and_cost_of_book()


