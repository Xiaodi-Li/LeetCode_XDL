# 1091. Shortest Path in Binary Matrix
# Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.
#
# A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:
#
# All the visited cells of the path are 0.
# All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
# The length of a clear path is the number of visited cells of this path.
from queue import Queue

class Shortest_Path_in_Binary_Matrix:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        m, n = len(grid), len(grid[0])
        dp = [[float('inf')] * n for _ in range(m)]
        dp[0][0] = 1

        queue = Queue()
        queue.put((0, 0))

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        while not queue.empty():
            i, j = queue.get()
            for dx, dy in directions:
                x = i + dx
                y = j + dy
                if 0 <= x < m and 0 <= y < n and grid[x][y] == 0 and dp[x][y] == float('inf'):
                    dp[x][y] = dp[i][j] + 1
                    queue.put((x, y))

        return dp[m - 1][n - 1] if dp[m - 1][n - 1] != float('inf') else -1


