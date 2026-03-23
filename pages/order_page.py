from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class OrderPage(BasePage):
    # Локаторы формы "Для кого самокат"
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_OPTION = (By.XPATH, "//div[@class='select-search__select']//button[contains(text(), '{}')]")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    # Локаторы формы "Про аренду"
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD = (By.CLASS_NAME, "Dropdown-control")
    RENTAL_OPTION = (By.XPATH, "//div[@class='Dropdown-menu']//div[text()='{}']")
    SCOOTER_COLOR_BLACK = (By.ID, "black")
    SCOOTER_COLOR_GREY = (By.ID, "grey")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Middle__1CSJM') and text()='Заказать']")
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")

    # Сообщение об успешном заказе
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader__3FDaJ') and text()='Заказ оформлен']")

    def __init__(self, driver):
        super().__init__(driver)

    def fill_order_form(self, order_data):
        """Заполняет форму заказа данными из словаря"""
        # Страница "Для кого самокат"
        self.send_keys(self.NAME_INPUT, order_data['name'])
        self.send_keys(self.SURNAME_INPUT, order_data['surname'])
        self.send_keys(self.ADDRESS_INPUT, order_data['address'])

        # Выбор станции метро
        self.click_element(self.METRO_STATION)
        metro_locator = (self.METRO_OPTION[0], self.METRO_OPTION[1].format(order_data['metro_station']))
        self.click_element(metro_locator)

        self.send_keys(self.PHONE_INPUT, order_data['phone'])
        self.click_element(self.NEXT_BUTTON)

        # Страница "Про аренду"
        self.send_keys(self.DATE_INPUT, order_data['date'])
        self.click_element(self.RENTAL_PERIOD)
        rental_locator = (self.RENTAL_OPTION[0], self.RENTAL_OPTION[1].format(order_data['rental_period']))
        self.click_element(rental_locator)

        if order_data['color'] == 'black':
            self.click_element(self.SCOOTER_COLOR_BLACK)
        elif order_data['color'] == 'grey':
            self.click_element(self.SCOOTER_COLOR_GREY)

        self.send_keys(self.COMMENT_INPUT, order_data['comment'])
        self.click_element(self.ORDER_BUTTON)
        self.click_element(self.CONFIRM_BUTTON)

    def get_success_message(self):
        return self.get_text(self.SUCCESS_MESSAGE)