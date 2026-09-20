import random

def generate_email():
    """Генерация уникального email по требованиям задания"""
    cohort_number = "19"  # Укажите ваш номер когорты
    random_digits = random.randint(100, 999)
    return f"yulia_test_{cohort_number}_{random_digits}@yandex.ru"

def generate_password(length=6):
    """Генерация случайного пароля заданной длины"""
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    return "".join(random.choice(chars) for _ in range(length))