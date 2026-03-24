import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открыть страницу {url}")
    def open(self, url):
        self.driver.get(url)

    @allure.step("Найти элемент {locator}")
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step("Кликнуть на элемент {locator}")
    def click_element(self, locator):
        self.find_element(locator).click()

    @allure.step("Ожидать URL {expected_url}")
    def wait_for_url(self, expected_url):
        self.wait.until(EC.url_to_be(expected_url))