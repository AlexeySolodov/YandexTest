import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="session")
def browser_options():
    """Опции запуска браузера"""
    chrome_options = Options()
    chrome_options.add_argument("--kiosk") # открытие во весь экран
    driver = webdriver.Chrome(executable_path="./chromedriver", options=chrome_options)
    yield driver
    driver.quit()