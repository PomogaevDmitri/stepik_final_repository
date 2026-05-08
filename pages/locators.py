from selenium.webdriver.common.by import By

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    BUTTON_TO_BASKET_IN_MAIN = (By.CSS_SELECTOR, ".btn-group a")
class BasketPageLocators:
    BASKET_TEXT_IN_TO_BASKET = (By.CSS_SELECTOR, "#content_inner p")
    BASKET_TOTALS = (By.CSS_SELECTOR, "#basket_totals")

class CataloguePageLocators:
    BUTTON_ADD_TO_CART = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRICE_PRODUCT = (By.CSS_SELECTOR, "p.price_color")
    PRICE_BASKET = (By.XPATH, "//*[@id='messages']/div[3]/div/p[1]/strong")
    DOP_URL_PROMO = f"catalogue/coders-at-work_207/?"
    NAME_PRODUCT = (By.CSS_SELECTOR, ".product_main h1")
    NAME_PRODUCT_IN_MESSAGE = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
    DOP_URL_THE_CITY = f"catalogue/the-city-and-the-stars_95/"

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    URL_LOGIN = 'login'
    BASKET_TO_EMPTY = (By.CSS_SELECTOR, ".basket-mini-item li p")
