import time
import pytest
from .pages.basket_page import BasketPage
from .pages.registration_page import RegistrationPage
from .pages.product_page import ProductPage


def test_guest_cant_see_success_message(browser):
    link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.need_review
def test_user_can_add_product_to_basket(browser):
    link = f"https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.add_item_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_sum_basket()
    page.should_be_name_product_to_basket()


@pytest.mark.parametrize('link_', ["offer0", "offer1", "offer2", "offer3", "offer4", "offer5", "offer6",
                                   pytest.param("offer7", marks=pytest.mark.xfail), "offer8", "offer9"])
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, link_):
    link = f"https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo={link_}"
    page = ProductPage(browser, link)
    page.open()
    page.add_item_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_sum_basket()
    page.should_be_name_product_to_basket()


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_item_to_basket()
    page.should_not_be_success_message()


def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_item_to_basket()
    time.sleep(1)
    page.should_not_be_success_message_is_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_in_the_basket_of_product()
    basket_page.should_be_text_empty_basket()


class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "https://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = RegistrationPage(browser, link)
        page.open()
        page.reg_account()

    def test_user_cant_see_success_message(self, browser):
        link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        link = f"https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, link)
        page.open()
        page.add_item_to_basket()
        page.solve_quiz_and_get_code()
        page.should_be_sum_basket()
        page.should_be_name_product_to_basket()
