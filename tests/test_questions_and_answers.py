import allure
import pytest
from locators.qa_locators import QAGLocators
from pages.main_page import MainPage
from data import AnswerText, Urls

class TestAG:

    @pytest.mark.parametrize("question_locator, answer_locator, expected_text", [
        (QAGLocators.QUESTION_1, QAGLocators.ANSWER_1, AnswerText.ANSWER_TEXT_1),
        (QAGLocators.QUESTION_2, QAGLocators.ANSWER_2, AnswerText.ANSWER_TEXT_2),
        (QAGLocators.QUESTION_3, QAGLocators.ANSWER_3, AnswerText.ANSWER_TEXT_3),
        (QAGLocators.QUESTION_4, QAGLocators.ANSWER_4, AnswerText.ANSWER_TEXT_4),
        (QAGLocators.QUESTION_5, QAGLocators.ANSWER_5, AnswerText.ANSWER_TEXT_5),
        (QAGLocators.QUESTION_6, QAGLocators.ANSWER_6, AnswerText.ANSWER_TEXT_6),
        (QAGLocators.QUESTION_7, QAGLocators.ANSWER_7, AnswerText.ANSWER_TEXT_7),
        (QAGLocators.QUESTION_8, QAGLocators.ANSWER_8, AnswerText.ANSWER_TEXT_8)
    ])
    @allure.description("Проверка ответа на вопрос.")
    def test_question_and_answer(self, driver, question_locator, answer_locator, expected_text):
        faq_page = MainPage(driver)
        faq_page.open_page(Urls.MAIN_PAGE)
        actual_text = faq_page.click_question_and_get_answer_text(question_locator, answer_locator)
        assert actual_text == expected_text, f"Текст на странице не соответствует ожидаемому: {expected_text}"
