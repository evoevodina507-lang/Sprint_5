import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators


class TestLogin:

    # Данные для входа в существующий аккаунт
    USER_EMAIL = "pipa2@mail.ru"
    USER_PASSWORD = "1234567"

    def helper_login_process(self, driver):
        """Вспомогательный метод для ввода почты, пароля и клика по кнопке 'Войти'"""
        driver.find_element(*TestLocators.EMAIL_INPUT_LOGIN).send_keys(
            self.USER_EMAIL
        )
        driver.find_element(*TestLocators.PASSWORD_INPUT_LOGIN).send_keys(
            self.USER_PASSWORD
        )
        driver.find_element(*TestLocators.LOGIN_SUBMIT_BUTTON).click()

    def test_login_from_main_page_button(self, driver):
        """1. Вход по кнопке 'Войти в аккаунт' на главной странице"""
        driver.get("https://stellarburgers.education-services.ru/")

        # Клик на кнопку "Войти в аккаунт"
        driver.find_element(*TestLocators.LOGIN_ACCOUNT_BUTTON).click()

        # Авторизация
        self.helper_login_process(driver)

        # Проверка, что успешно перешли на главную и видна кнопка "Оформить заказ"
        WebDriverWait(driver, 5).until(
            EC.url_to_be("https://stellarburgers.education-services.ru/")
        )
        assert (
            driver.current_url
            == "https://stellarburgers.education-services.ru/"
        )

    def test_login_from_personal_cabinet_button(self, driver):
        """2. Вход через кнопку 'Личный кабинет' в шапке сайта"""
        driver.get("https://stellarburgers.education-services.ru/")

        # Клик на "Личный Кабинет"
        driver.find_element(*TestLocators.PERSONAL_CABINET_BUTTON).click()

        # Авторизация
        self.helper_login_process(driver)

        # Проверка перехода на главную
        WebDriverWait(driver, 5).until(
            EC.url_to_be("https://stellarburgers.education-services.ru/")
        )
        assert (
            driver.current_url
            == "https://stellarburgers.education-services.ru/"
        )

    def test_login_from_registration_form_link(self, driver):
        """3. Вход через кнопку 'Войти' в форме регистрации"""
        driver.get("https://stellarburgers.education-services.ru/register")

        # Клик по ссылке/кнопке "Войти" на странице регистрации
        driver.find_element(*TestLocators.LOGIN_LINK_ON_REGISTER).click()

        # Авторизация
        self.helper_login_process(driver)

        # Проверка перехода на главную
        WebDriverWait(driver, 5).until(
            EC.url_to_be("https://stellarburgers.education-services.ru/")
        )
        assert (
            driver.current_url
            == "https://stellarburgers.education-services.ru/"
        )

    def test_login_from_forgot_password_form_link(self, driver):
        """4. Вход через кнопку 'Войти' в форме восстановления пароля"""
        driver.get(
            "https://stellarburgers.education-services.ru/forgot-password"
        )

        # Клик по ссылке/кнопке "Войти" на странице восстановления пароля
        driver.find_element(
            *TestLocators.LOGIN_LINK_ON_FORGOT_PASSWORD
        ).click()

        # Авторизация
        self.helper_login_process(driver)

        # Проверка перехода на главную
        WebDriverWait(driver, 5).until(
            EC.url_to_be("https://stellarburgers.education-services.ru/")
        )
        assert (
            driver.current_url
            == "https://stellarburgers.education-services.ru/"
        )