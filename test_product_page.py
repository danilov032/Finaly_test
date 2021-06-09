import time
import pytest
from .pages.product_page import ProductPage


@pytest.mark.parametrize('link_', ["offer0", "offer1", "offer2", "offer3", "offer4", "offer5", "offer6",
                                   pytest.param("offer7", marks=pytest.mark.xfail), "offer8", "offer9"])
def test_guest_can_add_product_to_basket(browser, link_):
    link = f" http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo={link_}"
    page = ProductPage(browser, link)
    page.open()
    page.add_item_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_sum_basket()
    page.should_be_name_product_to_basket()
    # time.sleep(10)
