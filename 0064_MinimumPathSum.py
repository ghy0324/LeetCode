class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        ans = grid[:]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    ans[i][j] += ans[i][j - 1]
                elif j == 0:
                    ans[i][j] += ans[i - 1][j]
                else:
                    ans[i][j] += min(ans[i][j - 1], ans[i - 1][j])
        return ans[m - 1][n - 1]