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

# 987. Vertical Order Traversal of a Binary Tree
# Given the root of a binary tree, calculate the vertical order traversal of the binary tree.
#
# For each node at position (row, col), its left and right children will be at positions (row + 1, col - 1) and (row + 1, col + 1) respectively. The root of the tree is at (0, 0).
#
# The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values.
#
# Return the vertical order traversal of the binary tree.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Vertical_Order_Traversal:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        node_list = []

        def BFS(node):
            queue = collections.deque([(root, 0, 0)])
            while queue:
                node, row, col = queue.popleft()
                if node:
                    node_list.append((col, row, node.val))
                    queue.append((node.left, row + 1, col - 1))
                    queue.append((node.right, row + 1, col + 1))

        BFS(root)
        node_list.sort()
        ret = OrderedDict()

        for col, row, val in node_list:
            if col in ret:
                ret[col].append(val)
            else:
                ret[col] = [val]

        return ret.values()

# 199. Binary Tree Right Side View
# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Binary_Tree_Right_Side_View_B:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: return []
        next_level = collections.deque([root, ])
        rightside = []

        while next_level:
            curr_level = next_level
            next_level = collections.deque()

            while curr_level:
                node = curr_level.popleft()

                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            rightside.append(node.val)

        return rightside