from selenium.webdriver.common.by import By

class TestLocators:
    # --- Главная страница ---
    LOGIN_ACCOUNT_BUTTON = (By.XPATH, ".//button[text()='Войти в аккаунт']")
    PERSONAL_CABINET_BUTTON = (By.XPATH, ".//p[text()='Личный Кабинет']")
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text()='Конструктор']")
    LOGO_BUTTON = (By.XPATH, ".//div[contains(@class,'AppHeader_header__logo')]/a")

    # --- Форма входа (/login) ---
    EMAIL_INPUT_LOGIN = (By.XPATH, ".//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT_LOGIN = (By.XPATH, ".//label[text()='Пароль']/following-sibling::input")
    LOGIN_SUBMIT_BUTTON = (By.XPATH, ".//button[text()='Войти']")
    REGISTER_LINK_ON_LOGIN = (By.XPATH, ".//a[@href='/register']")
    FORGOT_PASSWORD_LINK = (By.XPATH, ".//a[@href='/forgot-password']")

    # --- Форма регистрации (/register) ---
    NAME_INPUT_REGISTER = (By.XPATH, ".//label[text()='Имя']/following-sibling::input")
    EMAIL_INPUT_REGISTER = (By.XPATH, ".//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT_REGISTER = (By.XPATH, ".//label[text()='Пароль']/following-sibling::input")
    REGISTER_SUBMIT_BUTTON = (By.XPATH, ".//button[text()='Зарегистрироваться']")
    LOGIN_LINK_ON_REGISTER = (By.XPATH, ".//a[@href='/login']")
    INCORRECT_PASSWORD_ERROR = (By.XPATH, ".//p[text()='Некорректный пароль']")

    # --- Форма восстановления пароля (/forgot-password) ---
    LOGIN_LINK_ON_FORGOT_PASSWORD = (By.XPATH, ".//a[@href='/login']")

    # --- Личный кабинет (/account/profile) ---
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")  # или (By.XPATH, "//*[text()='Выход']")

    # --- Раздел «Конструктор» (вкладки) ---
    BUNS_TAB = (By.XPATH, ".//span[text()='Булки']/parent::div")
    SAUCES_TAB = (By.XPATH, ".//span[text()='Соусы']/parent::div")
    FILLINGS_TAB = (By.XPATH, ".//span[text()='Начинки']/parent::div")
    ACTIVE_TAB = (By.XPATH, ".//div[contains(@class, 'tab_tab_type_current')]/span")