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

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):

    product_page = ProductPage(browser, link)
    product_page.open()

    product_page.should_be_button_add_to_basket()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.check_added_to_basket()


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):

    product_page = ProductPage(browser, link)
    product_page.open()

    product_page.should_be_button_add_to_basket()
    product_page.add_to_basket()


