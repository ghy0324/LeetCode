class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if max(nums) <= 0:
            return max(nums)
        ans, sum_ = 0, 0
        for i in nums:
            sum_ += i
            sum_ = max(sum_, 0)
            ans = max(ans, sum_)
        return ans
