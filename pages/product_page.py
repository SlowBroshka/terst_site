from .base_page import BasePage
from .locators import ProductPageLocators as Ppl

import time


class ProductPage(BasePage):

    def should_be_button_add_to_basket(self):
        assert self.is_elem_present(*Ppl.BASKET_BUTTON), \
            "Fail to find basket button "

    def add_to_basket(self):
        bask_button = self.browser.find_element(*Ppl.BASKET_BUTTON)
        bask_button.click()
        time.sleep(1)
