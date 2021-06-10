from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_text_empty_basket(self):
        text_empty = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY).text
        num = text_empty.find("basket is empty")
        assert num != -1, "Корзина не пуста"

    def should_not_be_in_the_basket_of_product(self):
        assert self.is_not_element_present(*BasketPageLocators.NAME_PRODUCT), "В корзине есть товар!"
