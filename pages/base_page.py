from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)

    def wait_and_find_element(self, locator):
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(locator)
        )
        return self.driver.find_element(*locator)

    def scroll_and_click(self, locator):
        element = self.wait_and_find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.execute_script("arguments[0].click();", element)

    def click_element(self, locator):
        element = self.wait_and_find_element(locator)
        element.click()
        return element
