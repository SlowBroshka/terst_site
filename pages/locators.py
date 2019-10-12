from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_URL = "login"


class ProductPageLocators():
    BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p.price_color")
    BASKET_PRICE  = (By.CSS_SELECTOR, ".alert-info strong")
    PRODUCT_MAIN  = (By.CSS_SELECTOR, ".product_main h1")
    BASKET_ADDED  = \
        (By.CSS_SELECTOR, "#messages .alert-success:nth-child(1) strong")

