import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class OrderPage(BasePage):
    # Локаторы
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    # ... другие локаторы

    @allure.step("Выбрать станцию метро {station_name}")
    def select_metro_station(self, station_name):
        self.click_element(self.METRO_STATION)
        # Динамический поиск по тексту
        metro_option = (By.XPATH, f"//div[contains(@class, 'Order_Text__') and text()='{station_name}']")
        self.click_element(metro_option)

    @allure.step("Нажать кнопку 'Заказать' (позиция: {position})")
    def click_order_button(self, position):
        if position == "top":
            self.click_element(self.ORDER_TOP_BUTTON)
        elif position == "bottom":
            self.click_element(self.ORDER_BOTTOM_BUTTON)