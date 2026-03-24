import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class MainPage(BasePage):
    # Локаторы
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
    ORDER_TOP_BUTTON = (By.CLASS_NAME, "Button_Button__ra12g")
    ORDER_BOTTOM_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and text()='Заказать']")
    SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")

    BASE_URL = "https://qa-scooter.praktikum-services.ru/"

    @allure.step("Открыть главную страницу")
    def open(self):
        super().open(self.BASE_URL)

    @allure.step("Принять куки")
    def accept_cookies(self):
        self.click_element(self.COOKIE_BUTTON)

    @allure.step("Нажать верхнюю кнопку 'Заказать'")
    def click_order_top(self):
        self.click_element(self.ORDER_TOP_BUTTON)

    @allure.step("Нажать нижнюю кнопку 'Заказать'")
    def click_order_bottom(self):
        self.click_element(self.ORDER_BOTTOM_BUTTON)

    @allure.step("Нажать логотип Самоката")
    def click_scooter_logo(self):
        self.click_element(self.SCOOTER_LOGO)