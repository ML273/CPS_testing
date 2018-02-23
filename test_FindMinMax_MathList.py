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
    from mathlist import MathList
    list1 = list(range(1, 11))
    x = MathList(list1)
    assert x.min_max == (1, 10)


def test_negative_numbers():
    from mathlist import MathList
    list2 = list(range(-12, -1))
    x = MathList(list2)
    assert x.min_max == (-12, -2)


def test_floats():
    from mathlist import MathList
    list3 = np.arange(-1.0, 1.1, 0.1)
    x = MathList(list3)
    tup = x.min_max
    assert abs(tup[0] + 1.0) < 0.00001
    assert abs(tup[1] - 1.0) < 0.00001


def test_fractions():
    from mathlist import MathList
    list4 = np.arange(1/3, 5/3, 1/3)
    x = MathList(list4)
    tup = x.min_max
    assert abs(tup[0] - 1/3) < 0.00001
    assert abs(tup[1] - 5/3) < 0.00001
