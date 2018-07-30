class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        ans = [[1] * n] * m
        for i in range(0, m):
            for j in range(0, n):
                if obstacleGrid[i][j] == 1:
                    ans[i][j] = 0
                elif i == 0 and j == 0:
                    ans[i][j] = 1
                else:
                    ans[i][j] = (ans[i - 1][j] if i != 0 else 0) + (ans[i][j - 1] if j != 0 else 0)
        return ans[m - 1][n - 1]