import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from pages.main_page import MainPage
from pages.order_page import OrderPage

@pytest.fixture
def driver():
    # Настройка драйвера Firefox
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://qa-scooter.praktikum-services.ru/")
    # Создаем страницы для использования в тестах
    main_page = MainPage(driver)
    main_page.accept_cookies()
    yield driver
    driver.quit()

@pytest.fixture
def main_page(driver):
    return MainPage(driver)

@pytest.fixture
def order_page(driver):
    return OrderPage(driver)