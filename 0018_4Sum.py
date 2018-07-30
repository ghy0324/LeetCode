class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        nums.sort()
        for i in range(len(nums) - 3):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] > target // 4:
                break
            for j in range(i + 1, len(nums) - 2):
                if j != i + 1 and nums[j] == nums[j - 1]:
                    continue
                if nums[j] > (target - nums[i]) // 3:
                    break
                k = j + 1
                l = len(nums) - 1
                while k < l:
                    val = nums[i] + nums[j] + nums[k] + nums[l]
                    if val < target:
                        k += 1
                    elif val > target:
                        l -= 1
                    else:
                        ans.append([nums[i], nums[j], nums[k], nums[l]])
                        while k < l and nums[k + 1] == nums[k]:
                            k += 1
                        k += 1
                        while l > k and nums[l - 1] == nums[l]:
                            l -= 1
                        l -= 1
        return ans