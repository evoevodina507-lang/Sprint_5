def test_chrome_open(driver):
    driver.get("https://stellarburgers.education-services.ru/")
    assert "Stellar Burgers" in driver.title