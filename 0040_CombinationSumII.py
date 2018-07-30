class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        if target in candidates:
            ans.append([target])
        candidates = [i for i in candidates if i < target]
        if not candidates:
            return ans
        candidates.sort()
        for i in range(len(candidates)):
            if i != 0 and candidates[i] == candidates[i - 1]:
                continue
            ans += [[candidates[i]] + j for j in self.combinationSum2(candidates[i + 1:], target - candidates[i])]
        return ans