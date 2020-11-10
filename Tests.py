from YandexTest import TestSearchText, TestSearchPicture


def test_yandex_text(browser_options):
    yandex_search = TestSearchText(browser_options)  # Открытие браузера
    yandex_search.go_to_site()  # Переход на сайт
    yandex_search.test_search_field()  # Нахождение
    yandex_search.test_suggest_field('Совкомбанк')  # Вбиваем нужное слово и проверяем что получили поле подсказок
    sug_word = yandex_search.test_suggest_word('Совкомбанк')  # Проверяем что нужное слово есть в подсказках
    assert sug_word, "Can't find word in suggest "
    yandex_search.test_search_complite()  # Проверка наличий результатов поиска
    results = yandex_search.test_search_result('sovcombank.ru')  # Ищем слово
    assert results, "Can't find word in result"  # Ищем слово

def test_yandex_picture(browser_options):
    yandex_search = TestSearchPicture(browser_options)  # Открытие браузера
    yandex_search.go_to_site()  # Переход на сайт
    yandex_search.test_button('Картинки')  # Проверка наличия нужной кнопки
    result_link = yandex_search.test_link()  # Переход в новое окно
    assert 'https://yandex.ru/images/' in result_link, "Wrong link (exeption: 'https://yandex.ru/images/')"
    yandex_search.test_popular_request()  # Переход в рубрику популярное
    first_pic = yandex_search.test_first_picture()  # Открытие первой картинки и сохранение ссылки
    second_pic = yandex_search.test_second_picture()  # Открытие второй картинки и сохранение ссылки
    assert first_pic != second_pic, "did not switch to another picture"  # Проверяем что открылась другая картинка
    back_pic = yandex_search.test_back_picture()  # Переход назад
    assert back_pic == first_pic, "did not switch to first picture"  # Проверяем переход на первую картинку
