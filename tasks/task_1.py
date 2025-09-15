# ЗАДАНИЕ 1: Логирование вызова функции
# Напиши декоратор log, который:
# - печатает имя вызываемой функции и переданные
#  ей аргументы,
# - затем вызывает оригинальную функцию,
# - после этого печатает возвращённый результат.
# Пример:
# >>> @log
# >>> def add(a, b): return a + b
# >>> add(2, 3)
# Вывод:
# Вызов: add(2, 3)
# Результат: 5

from functools import wraps


def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = ", ".join(repr(arg) for arg in args)
        kwargs_repr = ", ".join(f"{k}={v!r}" for k, v in kwargs.items())
        all_args = ", ".join(filter(None, [args_repr, kwargs_repr]))
        print(f"Вызов: {func.__name__}({all_args})")
        result = func(*args, **kwargs)
        print(f"Результат: {result}")
        return result

    return wrapper
