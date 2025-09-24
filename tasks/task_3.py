from functools import wraps
import numbers


def validate_positive(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for i, arg in enumerate(args, start=1):
            if isinstance(arg, numbers.Real) and arg <= 0:
                raise ValueError("Все аргументы должны быть положительными")
            # меняю текст, чтобы дать понять в чем ошибка
            # но пайтест просит возврат с таким текстом

        for name, arg in kwargs.items():
            if isinstance(arg, numbers.Real) and arg <= 0:
                raise ValueError("Все аргументы должны быть положительными")

        return func(*args, **kwargs)
    return wrapper
