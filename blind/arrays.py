class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp is dict:
                return [i, dict[nums[i]]]
            dict[comp] = nums[i]

    def maxProfit(self, prices: List[int]) -> int:
        l = float('inf')
        h = 0
        for i in range(len(prices)):
            if prices[i] < l:
                l = prices[i]
            elif prices[i] > h:
                h = prices[i] - l
        return h

    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False
    
    def containsDuplicateAgain(self, nums: List[int]) -> bool:
        visited = set()
        for n in nums:
            if n in visited:
                return True
            visited.add(n)
        return False

    def productOfArrayExeptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        pre = 1
        for i in range(len(nums)):
            res[i] = pre
            pre *= nums[i]
        post = 1
        for i in reversed(range(len(nums))):
            res[i] *= post
            post *= nums[i]
        return res

    def findMinimumInRotatedSortedArray(self, nums: List[int]) -> int:
        
    def searchInRotatedSortedArray(self, nums: List[int]) -> int:

    def treeSum(self, nums: List[int]) -> int: 

    def containerWithMostWater(self, heights: List[int]) -> List[int]:
