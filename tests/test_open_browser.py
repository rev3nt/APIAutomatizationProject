from selenium import webdriver
from selenium.webdriver.common.by import By

import time


# Тест для открытия ссылки в браузере
def test_open_browser():
    # URL сайта, на который необходимо зайти
    url = 'https://vkusnoitochka.ru'

    # Настраиваем браузер таким образом, чтобы он сразу не закрывался после исполнения скрипта
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    # Создаем драйвер, загружаем в него настройки
    driver = webdriver.Chrome(options=options)

    # Открываем ссылку в браузере и разворачиваем его на полный экран
    driver.get(url)
    driver.maximize_window()

    # Создаем текст, который должен отображаться на открытой странице
    expected_text = 'Приложение'
    # Находим локатор нужного элемента и извлекаем из него текст
    success_text = driver.find_element(By.XPATH, f'//p[contains(text(), {expected_text})]').text
    print(success_text)

    # Добавляем проверку, что текст соответствует ожидаемому результату
    assert success_text == expected_text
    print("Сайт был успешно открыт!")

    # Добавляем небольшое ожидание
    time.sleep(3)

    # Закрываем браузер
    driver.quit()