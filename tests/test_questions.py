import allure
import pytest
from data.questions_data import questions, answers
from pages.main_page import MainPage

@allure.feature("Вопросы и ответы")
class TestQuestions:
    @pytest.mark.parametrize("index", range(len(questions)))
    def test_questions(self, driver, index):
        main_page = MainPage(driver)
        main_page.open()
        main_page.accept_cookies()
        # ... логика раскрытия вопроса и проверки текста ответа
        # Используем questions[index] и answers[index]