class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] > 0:
                break
            j = i + 1
            k = len(nums) - 1
            while j < k and nums[k] >= 0:
                val = nums[i] + nums[j] + nums[k]
                if val > 0:
                    k -= 1
                elif val < 0:
                    j += 1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j + 1] == nums[j]:
                        j += 1
                    j += 1
                    while k > j and nums[k - 1] == nums[k]:
                        k -= 1
                    k -= 1
        return ans