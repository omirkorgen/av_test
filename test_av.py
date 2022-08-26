from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


def get_url(url: str) -> str:
    """Функция выполняет поиск билетов
       и возвращает текст из text_reg
       при успешном поиске.
    """
    browser = webdriver.Chrome()
    browser.get(url)

    step1 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Откуда']")
    # нажимает на поле ввода "откуда"
    step1.click()
    time.sleep(1)
    step2 = browser.find_element(By.CSS_SELECTOR, "[data-qa-id='desktop-main-city-from'] .pt-2 li:nth-child(2)")
    # выбирает из выпадающего списка второй элемент
    step2.click()
    time.sleep(1)
    step3 = browser.find_element(By.CSS_SELECTOR, "[data-qa-id='desktop-main-city-to'] .pt-2 li:nth-child(4)")
    # выбирает из выпадающего списка четвертый элемент
    step3.click()
    button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    # нажимает на кнопку "найти"
    button.click()
    time.sleep(2)
    text_reg = browser.find_element(By.CSS_SELECTOR, "[class='text-base mb-4']").text
    browser.quit()
    return text_reg


class TestRegistration(unittest.TestCase):
    def test_registration1(self):
        text = get_url('https://aviata.kz/')
        self.assertEqual("Цена указана за всех пассажиров • Время вылета и прилета местное", text)


if __name__ == "__main__":
    unittest.main()


