from functools import wraps
from collections import OrderedDict


def simple_cache(func=None, *, maxsize=128):
    def make_hashable(obj):
        if isinstance(obj, dict):
            return tuple(sorted((k, make_hashable(v)) for k, v in obj.items()))
        elif isinstance(obj, (list, set)):
            return tuple(make_hashable(v) for v in obj)
        elif isinstance(obj, tuple):
            return tuple(make_hashable(v) for v in obj)
        return obj

    def decorator(f):
        cache = OrderedDict()

        @wraps(f)
        def wrapper(*args, **kwargs):
            key = (make_hashable(args), make_hashable(kwargs))
            if key in cache:
                print("Из кэша")
                return cache[key]

            result = f(*args, **kwargs)
            cache[key] = result
            if len(cache) > maxsize:
                cache.popitem(last=False)
            return result

        return wrapper
    if func is not None and callable(func):
        return decorator(func)

    return decorator
