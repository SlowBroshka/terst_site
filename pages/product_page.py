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

    def check_added_to_basket(self):
        assert self.check_added_name(), \
            "Name error"
        assert self.check_added_price(), \
            "Price error"

    def check_added_price(self):
        main_price = str(self.find_product_price())
        basket_price = str(self.get_basket_price())
        assert  main_price == basket_price,  \
            "Price not equal Main price: {} Basket price: {}"\
                .format(main_price, basket_price)
        return True

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*Ppl.BASKET_ADDED), \
            "Success message is presented, but should not be"

    def check_added_name(self):
        main_name = str(self.get_product_main())
        basket_name = str(self.book_success_bunner())
        assert  main_name == basket_name,  \
            "Price not equal Main name: {} Basket name: {}"\
                .format(main_name, basket_name)
        return True

    def find_product_price(self):
        assert self.is_elem_present(*Ppl.PRODUCT_PRICE), \
            "Cannot find product price"
        return self.browser.find_element(*Ppl.PRODUCT_PRICE).text

    def get_basket_price(self):
        assert self.is_elem_present(*Ppl.BASKET_PRICE), \
            "Cannot find all basket price"
        return self.browser.find_element(*Ppl.BASKET_PRICE).text

    def book_success_bunner(self):
        assert self.is_elem_present(*Ppl.BASKET_ADDED), \
            "Cannot find basket added text"
        return self.browser.find_element(*Ppl.BASKET_ADDED).text

    def get_product_main(self):
        assert self.is_elem_present(*Ppl.PRODUCT_MAIN), \
            "Cannot find product main name"
        return self.browser.find_element(*Ppl.PRODUCT_MAIN).text
