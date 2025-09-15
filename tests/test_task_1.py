import builtins

from tasks import log


def test_log_output(capsys):
    @log
    def add(a, b):
        return a + b

    result = add(2, 3)
    captured = capsys.readouterr()

    assert result == 5
    assert "Вызов: add(2, 3)" in captured.out
    assert "Результат: 5" in captured.out
