import allure
import pytest
from pages.order_page import OrderPage

@allure.feature("Заказ самоката")
class TestOrder:
    @pytest.mark.parametrize("button", ["top", "bottom"])
    def test_order_success(self, main_page_object, order_page, button):
        # Используем main_page_object для действий на главной (без автоматического открытия)
        main_page_object.click_order_button(button)  # вызов метода с параметром
        # Дальнейшее заполнение формы через order_page
        order_page.fill_order_form()