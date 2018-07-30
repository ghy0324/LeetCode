class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        leftest = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= leftest:
                leftest = i
        return leftest == 0
