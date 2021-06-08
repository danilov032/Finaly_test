from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    MAIL_INPUT_IN_LOGIN = (By.CSS_SELECTOR, "#id_login-username")
    MAIL_INPUT_IN_REG = (By.CSS_SELECTOR, "#id_registration-email")
