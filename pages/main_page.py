from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class MainPage(BasePage):
    # Локаторы
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")  # Кнопка "да все привыкли" (куки)
    ORDER_TOP_BUTTON = (By.CLASS_NAME, "Button_Button__ra12g")  # Верхняя кнопка "Заказать"
    ORDER_BOTTOM_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")  # Нижняя кнопка "Заказать"
    QUESTION_LOCATOR = (By.ID, "accordion__heading-{}")  # Шаблон для вопроса
    ANSWER_LOCATOR = (By.ID, "accordion__panel-{}")     # Шаблон для ответа
    SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")

    def __init__(self, driver):
        super().__init__(driver)

    def accept_cookies(self):
        # Принимаем куки, если они есть (чтобы не мешали)
        try:
            self.click_element(self.COOKIE_BUTTON)
        except:
            pass

    def click_order_top(self):
        self.click_element(self.ORDER_TOP_BUTTON)

    def click_order_bottom(self):
        self.click_element(self.ORDER_BOTTOM_BUTTON)

    def click_question(self, index):
        """Клик по вопросу с индексом index (0-based)"""
        locator = (self.QUESTION_LOCATOR[0], self.QUESTION_LOCATOR[1].format(index))
        self.click_element(locator)

    def get_answer_text(self, index):
        """Получить текст ответа по индексу"""
        locator = (self.ANSWER_LOCATOR[0], self.ANSWER_LOCATOR[1].format(index))
        return self.get_text(locator)

    def click_scooter_logo(self):
        self.click_element(self.SCOOTER_LOGO)

    def click_yandex_logo(self):
        self.click_element(self.YANDEX_LOGO)