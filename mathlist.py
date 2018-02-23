class MathList():
    """Class that when given a list can provide the sum of the list, \
    a tuple of the min and max from the list, and the maximum difference \
    between two adjacent numbers in the list.

    :param list: Input that is a list of numbers. Can be integers or \
    floats
    """

    def __init__(self, list1=[1,2]):
        self.lists = list1
        self.sum_all = None #no value yet
        """float: Provides the sum of the input list"""
        self.min_max = None
        """float: Provides the minimum and maximum of the list as a tuple"""
        self.max_diff = None
        """float: Provides the greatest difference between\
        two adjacent numbers in a list"""
        self.summation() #call the functions
        self.findMinMax()
        self.maxDiff()

    def summation(self):
        """Function that when given a list can provide the sum of the list

        :param list: Input that is a list of numbers. Can be integers or \
        floats

        :returns: combined sum of a list of numbers
        :raises ImportError: an error is raised if numpy cannot be found
        :raises TypeError: an error is raised if the data input contains \
        combined data types or a string instead of integers or a list
        :raises ValueError: an error is raised if the data input contains \
        unsupported numerical values (i.e. an imaginary number or string)
        """
        from summation import summation
        self.sum_all = summation(self.lists)

    def findMinMax(self):
        """Function that when given a list can provide \
        a tuple of the min and max from the list

        :param list: Input that is a list of numbers. Can be integers or \
        floats

        :returns: a tuple of the min and max from the list
        :raises ImportError: an error is raised if logging cannot be found
        :raises TypeError: an error is raised if the data input contains \
        combined data types or a string instead of integers or a list
        :raises ValueError: an error is raised if the data input contains \
        unsupported numerical values (i.e. an imaginary number or string)
        """
        from FindMinMax import FindMinMax
        self.min_max = FindMinMax(self.lists)

    def maxDiff(self):
        """Function that when given a list provides the maximum difference \
        between two adjacent numbers in the list.

        :param list: Input that is a list of numbers. Can be integers or \
        floats

        :returns: the maximum difference between two adjacent numbers in the list
        :raises ImportError: an error is raised if math cannot be found
        :raises TypeError: an error is raised if the data input contains \
        combined data types or a string instead of integers or a list
        :raises ValueError: an error is raised if the data input contains \
        unsupported numerical values (i.e. an imaginary number or string)
        """
        from maxDifference import maxFindDiff
        self.max_diff = maxFindDiff(self.lists)
