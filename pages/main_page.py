from .base_page import BasePage
from .locators import MainPageLocators as Mpl
from selenium.webdriver.common.by import By


class MainPage(BasePage):

    def go_to_login_page(self):
        login_link = self.browser.find_element(*Mpl.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        assert self.is_elem_present(*Mpl.LOGIN_LINK),\
            "Fail to find login link"



