from .base_page import BasePage
from .locators import LoginPageLocators as Lpl

from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_form(self):
        assert self.is_elem_present(*Lpl.LOGIN_FORM), \
            "Fail find login forrm"

    def should_be_login_url(self):
        assert self.has_str_in_url(Lpl.LOGIN_URL),\
            "Url not contain \"{}\" in url. Current url: \"{}\""\
                .format(Lpl.LOGIN_URL, self.get_curr_url())

    def should_be_register_form(self):
        assert self.is_elem_present(*Lpl.REGISTER_FORM ),\
            "Fail find register form"

