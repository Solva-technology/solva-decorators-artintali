from functools import wraps


def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        def _short_repr(obj, max_len=80):
            text = repr(obj)
            return text if len(text) <= max_len else text[:max_len] + "..."

        args_repr = ", ".join(_short_repr(arg) for arg in args)
        kwargs_repr = ", ".join(f"{k}={_short_repr(v)}" for k, v in kwargs.items())
        all_args = ", ".join(filter(None, [args_repr, kwargs_repr]))

        print(f"Вызов: {func.__name__}({all_args})")

        try:
            result = func(*args, **kwargs)
        except Exception as e:
            print(f"Ошибка: {e!r}")
        else:
            print(f"Результат: {_short_repr(result)}")
            return result

    return wrapper
