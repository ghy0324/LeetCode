class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return [[nums[i]] + _ for i in range(len(nums)) for _ in self.permute(nums[:i] + nums[i+1:])] if nums else [[]]