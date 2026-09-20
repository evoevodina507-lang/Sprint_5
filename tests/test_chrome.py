from selenium import webdriver


def test_chrome():
    driver = webdriver.Chrome()

    driver.get("https://stellarburgers.education-services.ru/")

    assert "Stellar Burgers" in driver.title

    driver.quit()