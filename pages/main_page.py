from .base_page import BasePage
from .login_page import LoginPage
from .locators import MainPageLocators as Mpl
from selenium.webdriver.common.by import By


class MainPage(BasePage):

    def go_to_login_page(self):
        login_link = self.browser.find_element(*Mpl.LOGIN_LINK)
        login_link.click()
        return LoginPage(browser=self.browser, url=self.url,
                         search_t_sec=self.search_t_sec)

    def should_be_login_link(self):
        assert self.is_elem_present(*Mpl.LOGIN_LINK),\
            "Fail to find login link"



