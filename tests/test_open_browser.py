from selenium import webdriver
from selenium.webdriver.common.by import By

import time


def test_open_browser():
    url = 'https://vkusnoitochka.ru'

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()

    success_text = driver.find_element(By.XPATH, '//h1[contains(text(), "Приходи к нам!")]').text
    expected_text = 'Приходи к нам!'

    assert success_text == expected_text

    time.sleep(3)

    driver.quit()