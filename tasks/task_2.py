# ЗАДАНИЕ 2: Кэширование результатов
# Напиши декоратор simple_cache, который:
# - запоминает результат функции при вызове с конкретными аргументами,
# - при повторном вызове с теми же аргументами — возвращает сохранённый
# результат без повторного вычисления,
# - печатает "Из кэша" при использовании кэшированного значения.
# Подсказка: используй словарь для хранения результатов.

from functools import wraps


def simple_cache(func):
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))
        if key in cache:
            print("Из кэша")
            return cache[key]
        result = func(*args, **kwargs)
        cache[key] = result
        return result
    return wrapper
