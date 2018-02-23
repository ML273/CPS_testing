def main(list1, list2, list3):
    print("Max Difference is: " + maxFindDiff(list1))
    print("Summation Total is: " + summation(list2))
    print("FindMinMax: " + FindMinMax(list3))


def maxFindDiff(in1):
    from maxDifference import maxFindDiff
    out1 = maxFindDiff(in1)
    return out1


def summation(in2):
    from summation import summation
    out2 = summation(in2)
    return out2


def FindMinMax(in3):
    from FindMinMax import FindMinMax
    out3 = FindMinMax(in3)
    return out3
