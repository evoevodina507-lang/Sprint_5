import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    # Отключаем лишние уведомления и подгрузки
    options.add_argument('--disable-notifications')
    options.add_argument('--disable-popup-blocking')
    
    # Запускаем браузер
    browser = webdriver.Chrome(options=options)
    
    # ВАЖНО: Устанавливаем жесткие таймауты загрузки страниц и поиска элементов
    browser.set_page_load_timeout(15)  # Не ждать загрузку страницы дольше 15 секунд
    browser.implicitly_wait(3)         # Не ждать поиск ненайденных элементов дольше 3 секунд
    browser.maximize_window()
    
    yield browser
    
    browser.quit()