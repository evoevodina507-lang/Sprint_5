import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators


class TestConstructor:

    def test_tab_sauces_navigation(self, driver):
        """Переход к разделу 'Соусы'"""
        driver.get("https://stellarburgers.education-services.ru/")

        sauces_tab = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(TestLocators.SAUCES_TAB)
        )
        driver.execute_script("arguments[0].click();", sauces_tab)

        WebDriverWait(driver, 10).until(
            lambda d: "tab_tab_type_current" in d.find_element(*TestLocators.SAUCES_TAB).get_attribute("class")
        )
        assert "tab_tab_type_current" in driver.find_element(*TestLocators.SAUCES_TAB).get_attribute("class")

    def test_tab_fillings_navigation(self, driver):
        """Проверка перехода на вкладку 'Начинки'"""
        driver.get("https://stellarburgers.education-services.ru/")

        fillings_tab = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(TestLocators.FILLINGS_TAB)
        )
        driver.execute_script("arguments[0].click();", fillings_tab)

        WebDriverWait(driver, 10).until(
            lambda d: "tab_tab_type_current" in d.find_element(*TestLocators.FILLINGS_TAB).get_attribute("class")
        )
        assert "tab_tab_type_current" in driver.find_element(*TestLocators.FILLINGS_TAB).get_attribute("class")

    def test_tab_buns_navigation(self, driver):
        """Переход к разделу 'Булки'"""
        driver.get("https://stellarburgers.education-services.ru/")

        # Сначала переключаемся на Соусы
        sauces_tab = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(TestLocators.SAUCES_TAB)
        )
        driver.execute_script("arguments[0].click();", sauces_tab)
        WebDriverWait(driver, 10).until(
            lambda d: "tab_tab_type_current" in d.find_element(*TestLocators.SAUCES_TAB).get_attribute("class")
        )

        # Возвращаемся на Булки
        buns_tab = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(TestLocators.BUNS_TAB)
        )
        driver.execute_script("arguments[0].click();", buns_tab)
        WebDriverWait(driver, 10).until(
            lambda d: "tab_tab_type_current" in d.find_element(*TestLocators.BUNS_TAB).get_attribute("class")
        )
        assert "tab_tab_type_current" in driver.find_element(*TestLocators.BUNS_TAB).get_attribute("class")