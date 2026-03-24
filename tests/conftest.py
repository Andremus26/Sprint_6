import pytest
from selenium import webdriver
from pages.main_page import MainPage
from pages.order_page import OrderPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()  # или другой браузер
    yield driver
    driver.quit()

@pytest.fixture
def main_page(driver):
    """Фикстура, которая возвращает MainPage с открытой главной страницей и принятыми куками."""
    main_page = MainPage(driver)
    main_page.open()
    main_page.accept_cookies()
    return main_page

@pytest.fixture
def main_page_object(driver):
    """Просто объект MainPage без навигации — для тестов, где не нужна главная страница."""
    return MainPage(driver)

@pytest.fixture
def order_page(driver):
    """Объект OrderPage без навигации."""
    return OrderPage(driver)