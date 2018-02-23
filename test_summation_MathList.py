def test_summation():
    from mathlist import MathList
    summed_output = MathList([2, 7])
    summed_output2 = MathList([-2, 3])
    summed_output3 = MathList([-2, -3])
    summed_output4 = MathList([-5, 10.25])
    assert summed_output.sum_all == 9
    assert summed_output2.sum_all == 1
    assert summed_output3.sum_all == -5
    assert summed_output4.sum_all == 5.25
    assert (summed_output4.sum_all-5.25) < .00001


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
