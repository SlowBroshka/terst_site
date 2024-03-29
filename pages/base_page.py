import math
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout)\
                .until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True


    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print("Your code: {}".format(alert_text))
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
