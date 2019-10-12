from selenium.common.exceptions import *


class BasePage():

    def __init__(self, browser, url, search_t_sec=10):
        self.browser = browser
        self.url = url
        self.search_t_sec = search_t_sec
        self.browser.implicitly_wait(search_t_sec)

    def open(self):
        self.browser.get(self.url)

    def is_elem_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def has_str_in_url(self, str):
        return str in self.browser.current_url

    def get_curr_url(self):
        return self.browser.current_url
