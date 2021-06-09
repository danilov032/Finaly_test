from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    MAIL_INPUT_IN_LOGIN = (By.CSS_SELECTOR, "#id_login-username")
    MAIL_INPUT_IN_REG = (By.CSS_SELECTOR, "#id_registration-email")


class ProductPageLocator():
    BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRICE_PRODUCT = (By.CSS_SELECTOR, ".product_main  p.price_color")
    SUM_BASKET = (By.XPATH, "//div[contains(@class, 'alertinner')]/p/strong")
    NAME_PRODUCT = (By.CSS_SELECTOR, ".product_main  h1")
    NAME_PRODUCT_TO_BASKET = (By.XPATH, "(//div[contains(@class, 'alertinner')]/strong)[1]")
