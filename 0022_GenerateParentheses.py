class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = [[], ['()']]
        if n <= 1:
            return ans[n]
        for i in range(2, n + 1):
            ans.append([])
            ans[i] += ['(' + str0 + ')' for str0 in ans[i - 1]]
            for j in range(1, i):
                ans[i] += [str1 + str2 for str1 in ans[j] for str2 in ans[i - j]]
            ans[i] = list(set(ans[i]))
        return ans[n]