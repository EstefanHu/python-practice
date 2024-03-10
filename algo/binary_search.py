class Solution:
    def __init__(self, name):
        self.name = name
        self.values = [1, 3, 4, 8, 10, 18, 23, 40]

    def bs(self, target):

s = Solution('binary search')

assert s.bs(10) == 4
assert s.bs(40) == 7
assert s.bs(-1) == -1

print('All tests passed')
