from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini a.btn-default")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    MAIL_INPUT_IN_LOGIN = (By.CSS_SELECTOR, "#id_login-username")
    MAIL_INPUT_IN_REG = (By.CSS_SELECTOR, "#id_registration-email")


class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRICE_PRODUCT = (By.CSS_SELECTOR, ".product_main  p.price_color")
    SUM_BASKET = (By.XPATH, "//div[contains(@class, 'alertinner')]/p/strong")
    NAME_PRODUCT = (By.CSS_SELECTOR, ".product_main  h1")
    NAME_PRODUCT_TO_BASKET = (By.XPATH, "(//div[contains(@class, 'alertinner')]/strong)[1]")
    SUCCESS_MESSAGE = (By.XPATH, "(//div[contains(@class, 'alertinner')])[2]")


class BasketPageLocators():
    BASKET_EMPTY = (By.CSS_SELECTOR, "#content_inner")
    NAME_PRODUCT = (By.CSS_SELECTOR, ".basket-items h3 a")
