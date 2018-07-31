class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = [0]
        for i in range(n):
            m = 2 ** i
            ans += [_ + m for _ in reversed(ans)]
        return ans
