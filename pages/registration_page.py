import time

from .base_page import BasePage
from .locators import RegistratioPageLocators


class RegistrationPage(BasePage):

    def reg_account(self):
        email_new = str(time.time()) + "@fakemail.org"
        email = self.browser.find_element(*RegistratioPageLocators.EMAIL_INPUT)
        email.send_keys(email_new)

        password_new = "Makaka12345"
        password = self.browser.find_element(*RegistratioPageLocators.PASSWORD_INPUT)
        password.send_keys(password_new)

        password_repeat = self.browser.find_element(*RegistratioPageLocators.REPEAT_PASSWORD_INPUT)
        password_repeat.send_keys(password_new)

        self.browser.find_element(*RegistratioPageLocators.BUTTON_REG).click()

    def should_be_successful_registration(self):
        message = self.browser.find_element(*RegistratioPageLocators.REG_SUCCESS).text
        assert message == "Спасибо за регистрацию", "Сообщение об успешной регистрации ОТСУТСТВУЕТ!!!"
