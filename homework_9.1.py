# Implement a class Mathematician which is a helper class for doing math
# operations on lists
# The class doesn't take any attributes and only has methods:
#   - square_nums (takes a list of integers and returns the list of squares)
#   - remove_positives (takes a list of integers and returns it without
# positive numbers
#   - filter_leaps (takes a list of dates (integers) and removes those that
# are not 'leap years'


class Mathematician:
    # def __init__(self):
    #     # self.square_nums = []
    #     # self.remove_positives = []
    #     # self.filter_leaps = []

    def square_nums(self, nums):
        self.square_nums = []
        for num in nums:
            self.square_nums.append(num*num)
        return self.square_nums

    def remove_positives(self, numbers):
        self.remove_positives = []
        for num in numbers:
            if num < 0:
                self.remove_positives.append(num)
        return self.remove_positives

    def filter_leaps(self, years):
        self.filter_leaps = []
        for year in years:
            if year % 4 == 0 and year % 100 != 0:
                self.filter_leaps.append(year)
            elif year % 100 == 0 and year % 400 == 0:
                self.filter_leaps.append(year)
        return self.filter_leaps


m = Mathematician()

assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]
