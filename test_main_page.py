from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage

import pytest


@pytest.mark.skip(reason="no way of currently testing this")
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()

    login_page = LoginPage(browser, browser.current_url, page.search_t_sec)

    login_page.should_be_login_page()


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear/"

    product_page = ProductPage(browser, link)

    product_page.should_be_button_add_to_basket()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()


