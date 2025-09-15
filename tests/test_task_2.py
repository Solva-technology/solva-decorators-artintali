from tasks import simple_cache


def test_simple_cache(capsys):
    call_count = {"count": 0}

    @simple_cache
    def slow_add(a, b):
        call_count["count"] += 1
        return a + b

    assert slow_add(2, 3) == 5
    assert call_count["count"] == 1
    captured = capsys.readouterr()
    assert "Из кэша" not in captured.out

    assert slow_add(2, 3) == 5
    assert call_count["count"] == 1
    captured = capsys.readouterr()
    assert "Из кэша" in captured.out
