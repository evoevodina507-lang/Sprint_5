import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators
from helpers import generate_email, generate_password


class TestNavigation:

    def helper_register_and_login(self, driver):
        """Создание пользователя и авторизация"""
        email = generate_email()
        password = generate_password(6)

        # 1. Регистрация
        driver.get("https://stellarburgers.education-services.ru/register")
        
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.NAME_INPUT_REGISTER)
        ).send_keys("Юлия")
        driver.find_element(*TestLocators.EMAIL_INPUT_REGISTER).send_keys(email)
        driver.find_element(*TestLocators.PASSWORD_INPUT_REGISTER).send_keys(password)
        
        reg_btn = driver.find_element(*TestLocators.REGISTER_SUBMIT_BUTTON)
        driver.execute_script("arguments[0].click();", reg_btn)

        # Ждем перехода на форму логина
        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://stellarburgers.education-services.ru/login")
        )

        # 2. Логин
        email_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.EMAIL_INPUT_LOGIN)
        )
        email_input.clear()
        email_input.send_keys(email)

        pass_input = driver.find_element(*TestLocators.PASSWORD_INPUT_LOGIN)
        pass_input.clear()
        pass_input.send_keys(password)

        login_btn = driver.find_element(*TestLocators.LOGIN_SUBMIT_BUTTON)
        driver.execute_script("arguments[0].click();", login_btn)

        # Ждем перехода на главную
        WebDriverWait(driver, 15).until(
            EC.url_to_be("https://stellarburgers.education-services.ru/")
        )

    def test_go_to_personal_account(self, driver):
        """Переход в Личный кабинет"""
        self.helper_register_and_login(driver)

        cabinet_btn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(TestLocators.PERSONAL_CABINET_BUTTON)
        )
        driver.execute_script("arguments[0].click();", cabinet_btn)

        WebDriverWait(driver, 15).until(EC.url_contains("/account"))
        assert "/account" in driver.current_url

    def test_go_from_personal_account_to_constructor(self, driver):
        """Переход из Личного кабинета в Конструктор"""
        self.helper_register_and_login(driver)

        cabinet_btn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(TestLocators.PERSONAL_CABINET_BUTTON)
        )
        driver.execute_script("arguments[0].click();", cabinet_btn)
        WebDriverWait(driver, 15).until(EC.url_contains("/account"))

        constructor_btn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(TestLocators.CONSTRUCTOR_BUTTON)
        )
        driver.execute_script("arguments[0].click();", constructor_btn)

        WebDriverWait(driver, 15).until(
            EC.url_to_be("https://stellarburgers.education-services.ru/")
        )
        assert driver.current_url == "https://stellarburgers.education-services.ru/"

    def test_go_from_personal_account_by_logo(self, driver):
        """Переход из Личного кабинета по логотипу"""
        self.helper_register_and_login(driver)

        cabinet_btn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(TestLocators.PERSONAL_CABINET_BUTTON)
        )
        driver.execute_script("arguments[0].click();", cabinet_btn)
        WebDriverWait(driver, 15).until(EC.url_contains("/account"))

        logo_btn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(TestLocators.LOGO_BUTTON)
        )
        driver.execute_script("arguments[0].click();", logo_btn)

        WebDriverWait(driver, 15).until(
            EC.url_to_be("https://stellarburgers.education-services.ru/")
        )
        assert driver.current_url == "https://stellarburgers.education-services.ru/"

    def test_logout_from_personal_account(self, driver):
        """Выход из аккаунта"""
        self.helper_register_and_login(driver)

        cabinet_btn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(TestLocators.PERSONAL_CABINET_BUTTON)
        )
        driver.execute_script("arguments[0].click();", cabinet_btn)

        WebDriverWait(driver, 15).until(EC.url_contains("/account"))

        logout_btn = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(TestLocators.LOGOUT_BUTTON)
        )
        driver.execute_script("arguments[0].click();", logout_btn)

        WebDriverWait(driver, 15).until(
            EC.url_to_be("https://stellarburgers.education-services.ru/login")
        )
        assert driver.current_url == "https://stellarburgers.education-services.ru/login"