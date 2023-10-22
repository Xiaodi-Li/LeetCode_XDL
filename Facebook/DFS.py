# 301. Remove Invalid Parentheses
# Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.
#
# Return a list of unique strings that are valid with the minimum number of removals. You may return the answer in any order.
class Remove_Invalid_Parentheses:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        l, r = 0, 0

        def isValid(s):
            count = 0
            for ch in s:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1
                if count < 0:
                    return False
            return count == 0

        def dfs(s, start, l, r, ans):
            if l == 0 and r == 0:
                if isValid(s):
                    ans.append(s)
                return

            for i in range(start, len(s)):
                if i != start and s[i] == s[i - 1]:
                    continue

                curr = s[:i] + s[i + 1:]
                if r > 0 and s[i] == ')':
                    dfs(curr, i, l, r - 1, ans)
                elif l > 0 and s[i] == '(':
                    dfs(curr, i, l - 1, r, ans)

        for ch in s:
            l += ch == '('
            if l == 0:
                r += ch == ')'
            else:
                l -= ch == ')'

        ans = []
        dfs(s, 0, l, r, ans)
        return ans

# 200. Number of Islands
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
class Number_of_Islands:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        if m < 0: return 0
        n = len(grid[0])

        ans = 0
        for y in range(m):
            for x in range(n):
                if grid[y][x] == '1':
                    ans += 1
                    self.__dfs(grid, y, x, m, n)

        return ans

    def __dfs(self, grid, y, x, m, n):
        if y >= m or x >= n or y < 0 or x < 0 or grid[y][x] == '0':
            return
        grid[y][x] = '0'
        self.__dfs(grid, y + 1, x, m, n)
        self.__dfs(grid, y - 1, x, m, n)
        self.__dfs(grid, y, x + 1, m, n)
        self.__dfs(grid, y, x - 1, m, n)

# 129. Sum Root to Leaf Numbers
# You are given the root of a binary tree containing digits from 0 to 9 only.
#
# Each root-to-leaf path in the tree represents a number.
#
# For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
# Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.
#
# A leaf node is a node with no children.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Sum_Root_to_Leaf_Numbers_I:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        root_to_leaf = 0
        stack = [(root, 0)]

        while stack:
            root, curr_num = stack.pop()
            if root is not None:
                curr_num = curr_num * 10 + root.val
                if root.left is None and root.right is None:
                    root_to_leaf += curr_num
                else:
                    stack.append((root.right, curr_num))
                    stack.append((root.left, curr_num))

        return root_to_leaf


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Sum_Root_to_Leaf_Numbers_II:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def preorder(r, curr_num):
            nonlocal root_to_leaf
            if r:
                curr_num = curr_num * 10 + r.val

                if not (r.left or r.right):
                    root_to_leaf += curr_num

                preorder(r.right, curr_num)
                preorder(r.left, curr_num)

        root_to_leaf = 0
        curr_num = 0
        preorder(root, curr_num)
        return root_to_leaf

# 199. Binary Tree Right Side View
# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Binary_Tree_Right_Side_View_D:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: return []

        rightside = []

        def dfs(node, level):
            if level == len(rightside):
                rightside.append(node.val)
            for child in [node.right, node.left]:
                if child:
                    dfs(child, level + 1)

        dfs(root, 0)
        return rightside

