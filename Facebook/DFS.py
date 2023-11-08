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

# 489. Robot Room Cleaner
# You are controlling a robot that is located somewhere in a room. The room is modeled as an m x n binary grid where 0 represents a wall and 1 represents an empty slot.
#
# The robot starts at an unknown location in the room that is guaranteed to be empty, and you do not have access to the grid, but you can move the robot using the given API Robot.
#
# You are tasked to use the robot to clean the entire room (i.e., clean every empty cell in the room). The robot with the four given APIs can move forward, turn left, or turn right. Each turn is 90 degrees.
#
# When the robot tries to move into a wall cell, its bumper sensor detects the obstacle, and it stays on the current cell.
#
# Design an algorithm to clean the entire room using the following APIs:
#
# interface Robot {
#   // returns true if next cell is open and robot moves into the cell.
#   // returns false if next cell is obstacle and robot stays on the current cell.
#   boolean move();
#
#   // Robot will stay on the same cell after calling turnLeft/turnRight.
#   // Each turn will be 90 degrees.
#   void turnLeft();
#   void turnRight();
#
#   // Clean the current cell.
#   void clean();
# }
# Note that the initial direction of the robot will be facing up. You can assume all four edges of the grid are all surrounded by a wall.
# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
# class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Robot_Room_Cleaner:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        self.dfs(robot, 0, 0, 0, 1, set())

    def dfs(self, robot, x, y, direction_x, direction_y, visited):
        robot.clean()
        visited.add((x, y))

        for i in range(4):
            neighbor_x = x + direction_x
            neighbor_y = y + direction_y
            if (neighbor_x, neighbor_y) not in visited and robot.move():
                self.dfs(robot, neighbor_x, neighbor_y, direction_x, direction_y, visited)
                robot.turnLeft()
                robot.turnLeft()
                robot.move()
                robot.turnLeft()
                robot.turnLeft()
            robot.turnLeft()
            direction_x, direction_y = -direction_y, direction_x

# 114. Flatten Binary Tree to Linked List
# Given the root of a binary tree, flatten the tree into a "linked list":
#
# The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
# The "linked list" should be in the same order as a pre-order traversal of the binary tree.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Flatten_Binary_Tree:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def dfs(node):
            if not node: return None
            if not node.left and not node.right:
                return node
            leftTail = dfs(node.left)
            rightTail = dfs(node.right)

            if leftTail:
                leftTail.right = node.right
                node.right = node.left
                node.left = None

            return rightTail if rightTail else leftTail

        dfs(root)

# 1161. Maximum Level Sum of a Binary Tree
# Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.
#
# Return the smallest level x such that the sum of all the values of nodes at level x is maximal.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Maximum_Level_Sum_DFS:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node, level, sum_at_current_level):
            if not node: return

            if len(sum_at_current_level) == level:
                sum_at_current_level.append(node.val)
            else:
                sum_at_current_level[level] += node.val

            dfs(node.left, level + 1, sum_at_current_level)
            dfs(node.right, level + 1, sum_at_current_level)

        sum_at_current_level = []
        dfs(root, 0, sum_at_current_level)

        return 1 + sum_at_current_level.index(max(sum_at_current_level))


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Maximum_Level_Sum_BFS:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_sum, level, ans = float('-inf'), 0, 0

        q = collections.deque()
        q.append(root)

        while q:
            level += 1
            sum_of_current_level = 0
            for _ in range(len(q)):
                node = q.popleft()
                sum_of_current_level += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if max_sum < sum_of_current_level:
                max_sum, ans = sum_of_current_level, level

        return ans
