def test_summation():
    from assignment04 import summation
    list_ = ([8, -9, 10])
    summed_output = summation([2, 7])
    summed_output2 = summation([-2, 3])
    summed_output3 = summation([-2, -3])
    summed_output4 = summation([-5, 10.25])
    assert summed_output == 9
    assert summed_output2 == 1
    assert summed_output3 == -5
    assert summed_output4 == 5.25
    assert (summed_output4-5.25) < .00001


def test_exceptions():
    import pytest
    import math
    with pytest.raises(ImportError, message="Anticipated ImportError"):
        import anypackage
    with pytest.raises(TypeError, message="Anticipated TypeError"):
        int_list = 1 + [1, 2, 4]
        int_str = 3 + "hello"
        list_str = [1, 2, 4] + "hello"
    with pytest.raises(ValueError, message="Anticipated ValueError"):
        val = int("hello")
