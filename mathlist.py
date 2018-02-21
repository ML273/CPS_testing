class MathList():

    def __init__(self, list1=[1,2]):
        self.lists = list1
        self.sum_all = None #no value yet
        self.min_max = None
        self.max_diff = None
        self.summation() #call the functions
        self.findMinMax()
        self.maxDiff()

    def summation(self):
        from summation import summation
        self.sum_all = summation(self.lists)

    def findMinMax(self):
        from FindMinMax import FindMinMax
        self.min_max = FindMinMax(self.lists)

    def maxDiff(self):
        from maxDifference import maxFindDiff
        self.max_diff = maxFindDiff(self.lists)
