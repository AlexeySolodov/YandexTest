from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchMethods:
    """Класс поиска методов"""

    def __init__(self, driver):
        """Инициилизация вебдрайвера и ссылки сайта"""

        self.driver = driver
        self.base_url = 'http://www.yandex.ru'

    def find_element(self, locator, time=10):
        """Нахождение элемента по локатору"""

        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        """Нахождение нескольких элементов по локатору"""

        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def go_to_site(self):
        """Открытие сайта"""

        return self.driver.get(self.base_url)