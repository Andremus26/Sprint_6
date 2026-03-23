import allure
import pytest
from data.order_data import order_data_sets
from pages.main_page import MainPage
from pages.order_page import OrderPage

@allure.feature("Заказ самоката")
class TestOrder:

    @allure.title("Позитивный сценарий заказа: {data[name]}, кнопка {button}")
    @pytest.mark.parametrize("data", order_data_sets)
    @pytest.mark.parametrize("button", ["top", "bottom"])
    def test_order_success(self, driver, data, button):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        # Выбор кнопки заказа
        if button == "top":
            main_page.click_order_top()
        else:
            main_page.click_order_bottom()

        # Заполнение формы
        order_page.fill_order_form(data)

        # Проверка успешного создания заказа
        assert order_page.get_success_message() == "Заказ оформлен"