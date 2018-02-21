def test_MaxDiffr():
    from assignment04 import maxFindDiff
    listV = [1, 2, 3, 6, 10]
    maxxNum = maxFindDiff(listV)
    assert maxxNum == 4
    findPos = maxFindDiff(listV)
    assert findPos > 0
    listV2 = [1.1, 2.2, 3.6, 8.9]
    maxxNumFloat = maxFindDiff(listV2)
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
