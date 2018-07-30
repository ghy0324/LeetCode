class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = [0] * len(s)
        ans[-1] = 1 if s[-1] != '0' else 0
        if len(s) >= 2:
            ans[-2] = (ans[-1] + (1 if int(s[-2:]) <= 26 else 0)) if s[-2] != '0' else 0
        for i in range(len(s) - 3, -1, -1):
            ans[i] = (ans[i + 1] + (ans[i + 2] if int(s[i : i + 2]) <= 26 else 0)) if s[i] != '0' else 0
        return ans[0]