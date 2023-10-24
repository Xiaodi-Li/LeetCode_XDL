# 766. Toeplitz Matrix
# Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.
#
# A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.
class Toeplitz_Matrix:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])

        for i in range(m):
            for j in range(n):
                if i + 1 < m and j + 1 < n:
                    if matrix[i][j] != matrix[i + 1][j + 1]:
                        return False

        return True

# 348. Design Tic-Tac-Toe
# Assume the following rules are for the tic-tac-toe game on an n x n board between two players:
#
# A move is guaranteed to be valid and is placed on an empty block.
# Once a winning condition is reached, no more moves are allowed.
# A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.
# Implement the TicTacToe class:
#
# TicTacToe(int n) Initializes the object the size of the board n.
# int move(int row, int col, int player) Indicates that the player with id player plays at the cell (row, col) of the board. The move is guaranteed to be a valid move, and the two players alternate in making moves. Return
# 0 if there is no winner after the move,
# 1 if player 1 is the winner after the move, or
# 2 if player 2 is the winner after the move.
class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.board = [[0] * n for _ in range(n)]

    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = player
        for r in range(self.n):
            if all(self.board[r][c] == 1 for c in range(self.n)) or all(self.board[r][c] == 2 for c in range(self.n)):
                return player
        for c in range(self.n):
            if all(self.board[r][c] == 1 for r in range(self.n)) or all(self.board[r][c] == 2 for r in range(self.n)):
                return player
        l_diag = True
        for i in range(self.n):
            if self.board[i][i] != self.board[0][0] != 0 or self.board[i][i] == 0:
                l_diag = False
            else:
                continue
        r_diag = True
        for i in range(self.n):
            if self.board[i][self.n - i - 1] != self.board[0][self.n - 1] or self.board[i][self.n - i - 1] == 0:
                r_diag = False
            else:
                continue
        if l_diag == True or r_diag == True:
            return player
        return 0
# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)