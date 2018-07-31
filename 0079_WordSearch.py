class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def exist_start_with_ij(word, i, j):
            if board[i][j] != word[0] or used[i][j]:
                return False
            if len(word) == 1:
                return True
            used[i][j] = True
            if i != 0 and exist_start_with_ij(word[1:], i - 1, j):
                return True
            if i != m - 1 and exist_start_with_ij(word[1:], i + 1, j):
                return True
            if j != 0 and exist_start_with_ij(word[1:], i, j - 1):
                return True
            if j != n - 1 and exist_start_with_ij(word[1:], i, j + 1):
                return True
            used[i][j] = False
            return False
        
        m, n = len(board), len(board[0])
        used = [[False for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and exist_start_with_ij(word, i, j):
                    return True
        return False
