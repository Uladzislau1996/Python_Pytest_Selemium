import pytest
from .pages.main_page import MainPage
from .pages.product_page import PageObject

@pytest.mark.parametrize('link', ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail),"8", "9"])
def test_guest_can_add_product_to_basket(browser, link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page = MainPage(browser, link)
    page.open()
    page = PageObject(browser, link)
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_correct_name_and_cost_of_book()
