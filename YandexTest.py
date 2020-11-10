from MethodsApp import SearchMethods
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class TestSearchText(SearchMethods):
    """Задание №1: Текст"""

    def test_search_field(self):
        """Проверка наличия поля поиска"""

        self.search_field = self.find_element((By.ID, 'text'))
        return self.search_field

    def test_suggest_field(self, text):
        """Проверка наличия поля подсказок"""

        self.search_field.click()
        self.search_field.send_keys(text)
        self.suggest_field = self.find_element((By.XPATH, '/html/body/div[4]/ul/li[1]'))
        return self.suggest_field

    def test_suggest_word(self, text):
        """Проверка на наличе в подсказак слова"""

        words = self.find_elements((By.CLASS_NAME, 'mini-suggest__popup-content'))
        result = [word.text for word in words if f'{text}' in word.text]
        return result

    def test_search_complite(self):
        """Проверка того что при нажатие ENTER появляется результат поиска"""

        self.search_field.send_keys(Keys.ENTER)
        self.urls_count = self.find_elements((By.XPATH, '//*[@id="search-result"]'))
        return self.urls_count

    def test_search_result(self, text):
        """Проверка резульатта поиска"""

        result = [link.text for link in self.urls_count[:5] if f'{text}' in link.text]
        return result


class TestSearchPicture(SearchMethods):
    """Задание №2: Картинки"""

    def test_button(self, text):
        """Проверка: Наличие кнопки с ссылкой 'Картинки'"""

        self.picture_link = self.find_element((By.LINK_TEXT, text))
        return self.picture_link

    def test_link(self):
        """Переход в новое окно после клика и проверка что это окно - картинки"""

        self.picture_link.click()
        self.driver.switch_to_window(self.driver.window_handles[-1])  # переход на другое окно
        link = self.driver.current_url
        return link

    def test_popular_request(self):
        """Открытие первой популярной рубрики из предложенных"""

        popular_request = self.find_element((By.XPATH, '/html/body/div[5]/div[1]/div[1]/div/div/div[1]/div[1]/a'))  # первое популярное
        popular_request.click()
        return popular_request

    def test_first_picture(self):
        """Открытие первой кртинки и проверка что открылось"""

        image_button = self.find_element((By.CLASS_NAME, 'serp-item__link'))  # первое изображение
        image_button.click()
        time.sleep(5)  # Костыль для подгрузки картинки
        picture_src1 = self.find_element((By.CLASS_NAME, 'MMImage-Origin')).get_attribute('src')  # сурс изображения
        return picture_src1

    def test_second_picture(self):
        """Проверка того что при нажатии кнопки 'Вперёд' картинка изменилась"""

        right_arrow = self.find_element((By.XPATH, '/html/body/div[13]/div[1]/div/div/div[3]/div/div[1]/div[1]/div[4]')) # наличе правой кнопки
        right_arrow.click()
        picture_src2 = self.find_element((By.CLASS_NAME, 'MMImage-Origin')).get_attribute('src')  # сурс следующего изображения
        return picture_src2

    def test_back_picture(self):
        """Возвращаемся к предыдущей картинке"""

        left_arrow = self.find_element((By.XPATH, '/html/body/div[13]/div[1]/div/div/div[3]/div/div[1]/div[1]/div[1]'))
        left_arrow.click()
        picture_back = self.find_element((By.CLASS_NAME, 'MMImage-Origin')).get_attribute('src')
        return picture_back

