from types import List
from typing import Counter

class Arrays:
    def __init__(self, name):
        self.name = name

    def two_sum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            comp = taget - nums[i]
            if comp in dict:
                return [i, dict[comp]]
            dict[nums[i]] = i

    def valid_anagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        counter = Counter(s)
        for ch in t:
            counter[ch] -= 1
            if counter[ch] < 0:
                return False
        return True

    def contains_duplicates(self, nums: List[int]) -> bool:
        checked = set()
        for x in nums:
            if x in checked:
                return True
            checked.add(x)
        return False
