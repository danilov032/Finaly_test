from .base_page import BasePage
from .locators import ProductPageLocator


class ProductPage(BasePage):
    def add_item_to_basket(self):
        basket = self.browser.find_element(*ProductPageLocator.BASKET_BUTTON)
        basket.click()

    def should_be_sum_basket(self):
        price = self.browser.find_element(*ProductPageLocator.PRICE_PRODUCT).text
        sum_basket = self.browser.find_element(*ProductPageLocator.SUM_BASKET).text
        assert price == sum_basket, "Цены не соответствуют"

    def should_be_name_product_to_basket(self):
        name_product = self.browser.find_element(*ProductPageLocator.NAME_PRODUCT).text
        name_product_add_to_basket = self.browser.find_element(*ProductPageLocator.NAME_PRODUCT_TO_BASKET).text
        assert name_product == name_product_add_to_basket, "Название продукта не соответствует добавленному"