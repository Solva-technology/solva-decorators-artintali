import pytest

from tasks import validate_positive


@validate_positive
def multiply(a, b):
    return a * b

def test_validate_positive_ok():
    assert multiply(2, 3) == 6

def test_validate_positive_error():
    with pytest.raises(ValueError, match="Все аргументы должны быть положительными"):
        multiply(-1, 4)
