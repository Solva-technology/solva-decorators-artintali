# ЗАДАНИЕ 3: Проверка аргументов на положительность
# Напиши декоратор validate_positive, который:
# - проверяет, что все переданные числовые аргументы
# больше 0,
# - если хотя бы один из них ≤ 0 — выбрасывает
#  ValueError с сообщением "Все аргументы должны быть
# положительными".
# Пример:
# >>> @validate_positive
# >>> def multiply(a, b): return a * b
# >>> multiply(-1, 3)
# ValueError: Все аргументы должны быть положительными

from functools import wraps


def validate_positive(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg <= 0:
                raise ValueError("Все аргументы должны быть положительными")
        for arg in kwargs.values():
            if isinstance(arg, (int, float)) and arg <= 0:
                raise ValueError("Все аргументы должны быть положительными")

        return func(*args, **kwargs)
    return wrapper
