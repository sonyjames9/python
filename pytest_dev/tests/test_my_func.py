import time

import pytest
import pytest_dev.source.my_func as my_func_test


def test_add():
    result = my_func_test.add(2, 3)
    assert result == 5


def test_divide():
    result = my_func_test.divide(10, 5)
    assert result == 2


def test_divide_by_zero():
    # with pytest.raises(ZeroDivisionError):
    with pytest.raises(ValueError):
        my_func_test.divide(10, 0)
    # assert True


def test_add_strings():
    result = my_func_test.add("i like ", "burgers")
    assert result == "i like burgers"


@pytest.mark.slow
def test_very_slow():
    time.sleep(5)
    result = my_func_test.divide(10, 5)
    assert result == 2


@pytest.mark.skip(reason="This feature is broken")
def test_add():
    assert my_func_test.add(1, 2) == 3


@pytest.mark.xfail(reason="We know we cannot divide by zero")
def test_divide_by_zero_broken():
    my_func_test.divide(4, 0)
