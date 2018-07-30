class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return [[nums[i]] + _ for i in range(len(nums)) for _ in self.permuteUnique(nums[:i] + nums[i+1:]) if nums[i] not in nums[:i]] if nums else [[]]