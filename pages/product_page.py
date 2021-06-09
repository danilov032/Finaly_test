from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_item_to_basket(self):
        basket = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket.click()

    def should_be_sum_basket(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        sum_basket = self.browser.find_element(*ProductPageLocators.SUM_BASKET).text
        assert price == sum_basket, "Цены не соответствуют"

    def should_be_name_product_to_basket(self):
        name_product = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        name_product_add_to_basket = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_TO_BASKET).text
        assert name_product == name_product_add_to_basket, "Название продукта не соответствует добавленному"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_not_be_success_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"