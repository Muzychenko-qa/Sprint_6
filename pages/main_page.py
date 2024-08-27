from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.redirect_locators import RedirectLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    def click_question_and_get_answer_text(self, question_locator, answer_locator):
        self.scroll_and_click(question_locator)
        answer_element = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(answer_locator))

        return answer_element.text

    def redirect_to_main_page(self):
        self.click_element(RedirectLocators.HEADER_BUTTON_SCOOTER)

    def redirect_to_dzen(self):
        all_windows_before = self.driver.window_handles
        self.click_element(RedirectLocators.HEADER_BUTTON_YANDEX)
        all_windows_after = self.driver.window_handles
        new_tab = [window for window in all_windows_after if window not in all_windows_before][0]
        self.driver.switch_to.window(new_tab)
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(RedirectLocators.DZEN_PAGE))
