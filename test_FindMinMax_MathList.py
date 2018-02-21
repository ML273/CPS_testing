import numpy as np
import math
# https://docs.pytest.org/en/latest/assert.html
# Assertions about expected exceptions


def test_exceptions():
    import pytest
    with pytest.raises(ImportError, message="Expecting ImportError"):
        import blah
    with pytest.raises(TypeError, message="Expecting TypeError"):
        test = 5 + 'h'
    with pytest.raises(ValueError, message="Expecting ValueError"):
        test = math.sqrt(-1)


def test_positive_numbers():
    from assignment04 import FindMinMax
    list1 = list(range(1, 11))
    assert FindMinMax(list1) == (1, 10)


def test_negative_numbers():
    from assignment04 import FindMinMax
    list2 = list(range(-12, -1))
    assert FindMinMax(list2) == (-12, -2)


def test_floats():
    from assignment04 import FindMinMax
    list3 = np.arange(-1.0, 1.1, 0.1)
    tup = FindMinMax(list3)
    assert abs(tup[0] + 1.0) < 0.00001
    assert abs(tup[1] - 1.0) < 0.00001


def test_fractions():
    from assignment04 import FindMinMax
    list4 = np.arange(1/3, 5/3, 1/3)
    tup = FindMinMax(list4)
    assert abs(tup[0] - 1/3) < 0.00001
    assert abs(tup[1] - 5/3) < 0.00001
