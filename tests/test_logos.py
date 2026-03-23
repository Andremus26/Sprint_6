import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage

@allure.feature("Логотипы")
class TestLogos:

    @allure.title("Клик на логотип Самоката переводит на главную страницу")
    def test_scooter_logo(self, driver, main_page):
        # Сначала переходим на любую другую страницу, чтобы проверить переход
        main_page.click_order_top()  # переходим на страницу заказа
        main_page.click_scooter_logo()
        # Проверяем, что текущий URL - главная страница
        WebDriverWait(driver, 5).until(EC.url_to_be("https://qa-scooter.praktikum-services.ru/"))
        assert driver.current_url == "https://qa-scooter.praktikum-services.ru/"

    @allure.title("Клик на логотип Яндекса открывает Дзен в новой вкладке")
    def test_yandex_logo(self, driver, main_page):
        original_window = driver.current_window_handle
        main_page.click_yandex_logo()
        # Ждем появления новой вкладки
        WebDriverWait(driver, 5).until(EC.number_of_windows_to_be(2))
        # Переключаемся на новую вкладку
        for window_handle in driver.window_handles:
            if window_handle != original_window:
                driver.switch_to.window(window_handle)
                break
        # Проверяем, что URL содержит dzen.ru (главная страница Дзена)
        WebDriverWait(driver, 5).until(EC.url_contains("dzen.ru"))
        assert "dzen.ru" in driver.current_url