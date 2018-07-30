from functools import reduce

class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return reduce(lambda x,y:x*y, [m+n-2-i for i in range(m-1)], 1) // reduce(lambda x,y:x*y, [m-1-i for i in range(m-1)], 1)
    