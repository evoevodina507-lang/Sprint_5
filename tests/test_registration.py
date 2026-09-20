import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators
from helpers import generate_email, generate_password

class TestRegistration:

    def test_successful_registration(self, driver):
        """Успешная регистрация с валидными данными"""
        driver.get("https://stellarburgers.education-services.ru/register")

        # Заполнение полей
        driver.find_element(*TestLocators.NAME_INPUT_REGISTER).send_keys("Юлия")
        driver.find_element(*TestLocators.EMAIL_INPUT_REGISTER).send_keys(generate_email())
        driver.find_element(*TestLocators.PASSWORD_INPUT_REGISTER).send_keys(generate_password(6))

        # Нажатие на кнопку регистрации
        driver.find_element(*TestLocators.REGISTER_SUBMIT_BUTTON).click()

        # Ожидание перехода на страницу входа
        WebDriverWait(driver, 5).until(
            EC.url_to_be("https://stellarburgers.education-services.ru/login")
        )
        assert driver.current_url == "https://stellarburgers.education-services.ru/login"

    def test_registration_incorrect_password_show_error(self, driver):
        """Ошибка при вводе некорректного пароля (менее 6 символов)"""
        driver.get("https://stellarburgers.education-services.ru/register")

        driver.find_element(*TestLocators.NAME_INPUT_REGISTER).send_keys("Юлия")
        driver.find_element(*TestLocators.EMAIL_INPUT_REGISTER).send_keys(generate_email())
        driver.find_element(*TestLocators.PASSWORD_INPUT_REGISTER).send_keys("12345")  # 5 символов

        driver.find_element(*TestLocators.REGISTER_SUBMIT_BUTTON).click()

        # Проверка отображения сообщения об ошибке
        error_element = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(TestLocators.INCORRECT_PASSWORD_ERROR)
        )
        assert error_element.is_displayed()