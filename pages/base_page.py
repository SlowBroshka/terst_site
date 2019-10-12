from selenium.common.exceptions import *


class BasePage():

    def __init__(self, browser, url, search_t_sec=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(search_t_sec)

    def open(self):
        self.browser.get(self.url)

    def is_elem_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
