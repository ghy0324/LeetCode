class Solution:   
    def is_valid(self, row, col):
        for i in range(row):
            if self.board[i] == col or abs(i - row) == abs(self.board[i] - col):
                return False
        return True
    
    def format_(self):
        return [''.join(['Q' if self.board[i] == j else '.' for j in range(self.n)]) for i in range(self.n)]
    
    def find(self, row):
        if row == self.n:
            self.ans += 1
        else:
            for col in range(self.n):
                if self.is_valid(row, col):
                    self.board[row] = col
                    self.find(row + 1)

    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.n = n
        self.board = [-1] * n
        self.ans = 0
        self.find(0)
        return self.ans
