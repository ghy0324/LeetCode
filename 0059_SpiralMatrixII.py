class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        ans = [[0 for j in range(n)] for i in range(n)]
        num = 1
        start = 0
        m = n
        while True:
            if m == 0:
                return ans
            if m == 1:
                ans[start][start] = num
                return ans
            for i in range(m):
                ans[start][start + i] = num
                num += 1
            for i in range(1, m - 1):
                ans[start + i][n - 1 - start] = num
                num += 1
            for i in range(m):
                ans[n - 1 - start][n - 1 - start - i] = num
                num += 1
            for i in range(1, m - 1):
                ans[n - 1 - start - i][start] = num
                num += 1
            start += 1
            m -= 2