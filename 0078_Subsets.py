class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self.subsets(nums[1:]) + [[nums[0]] + _ for _ in self.subsets(nums[1:])] if nums else [[]]