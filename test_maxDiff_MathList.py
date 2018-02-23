def test_MaxDiffr():
    from mathlist import MathList
    listV = [1, 2, 3, 6, 10]
    x = MathList(listV)
    maxxNum = x.max_diff
    assert maxxNum == 4
    findPos = x.max_diff
    assert findPos > 0
    listV2 = [1.1, 2.2, 3.6, 8.9]
    x2 = MathList(listV2)
    maxxNumFloat = x2.max_diff
    assert maxxNumFloat == 5.3


def test_correctExcp():
    import pytest
    import math
    with pytest.raises(ImportError, message="Expecting ImportError"):
        import randomFunc
    with pytest.raises(TypeError, message="Expecting TypeError"):
        numTest = 1 + "e"
    with pytest.raises(ValueError, message="Expecting ValueError"):
        numTest = math.sqrt(-1)
