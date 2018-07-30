class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []
        if len(matrix) == 1:
            return matrix[0]
        if len(matrix[0]) == 1:
            return [i[0] for i in matrix]
        return matrix[0] + [matrix[i][-1] for i in range(1, len(matrix) - 1)] + matrix[-1][::-1] + [matrix[i][0] for i in range(len(matrix) - 2, 0, -1)] + self.spiralOrder([i[1:-1] for i in matrix[1:-1]])