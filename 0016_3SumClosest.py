class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        closest = abs(nums[0] + nums[1] + nums[2] - target)
        closest_val = nums[0] + nums[1] + nums[2]
        if closest == 0:
            return target
        for i in range(len(nums) - 2):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                val = nums[i] + nums[j] + nums[k]
                if abs(val - target) < closest:
                    closest = abs(val - target)
                    closest_val = val
                    if closest == 0:
                        return target
                if val < target:
                    j += 1
                else:
                    k -= 1
        return closest_val
                    