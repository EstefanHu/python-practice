class Solution:
    def __init__(self, name):
        self.name = name

    def ss(self, array):
        print('Sorting array: %a' %array)

s = Solution('selection sort')
s.ss([3, 5, 1, 80, 893, 8, 53, 78, 490, 87, 0])
