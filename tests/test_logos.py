import allure
import pytest
from pages.main_page import MainPage

@allure.feature("Логотипы")
class TestLogos:
    @allure.title("Переход по логотипу Самоката возвращает на главную")
    def test_click_scooter_logo(self, main_page):
        main_page.click_order_top()        # переходим на страницу заказа
        main_page.click_scooter_logo()     # клик по логотипу
        main_page.wait_for_url(MainPage.BASE_URL)  # проверяем URL через метод BasePage