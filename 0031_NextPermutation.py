class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        i = l - 1
        while i > 0:
            if nums[i] > nums[i-1]:
                break
            i -= 1
        if i == 0:
            nums.sort()
        else:
            j = l - 1
            while nums[j] <= nums[i - 1]:
                j -= 1
            tmp = nums[i-1:j] + nums[j+1:]
            tmp.sort()
            nums[i-1:] = [nums[j]] + tmp