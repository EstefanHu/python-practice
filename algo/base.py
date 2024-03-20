class Solution:
    def __init__(self, name):
        self.name = name

    def call_name(self):
        return self.name

s = Solution('')
print('Running %s' %s.call_name())
