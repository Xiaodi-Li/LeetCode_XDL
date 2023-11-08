# 938. Range Sum of BST
# Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Range_Sum_of_BST:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans = 0
        stack = [root]

        while stack:
            node = stack.pop()
            if node:
                if low <= node.val <= high:
                    ans += node.val
                if low < node.val:
                    stack.append(node.left)
                if node.val < high:
                    stack.append(node.right)

        return ans

# 236. Lowest Common Ancestor of a Binary Tree
# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
#
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Lowest_Common_Ancestor_of_BT:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root in (None, p, q): return root
        left, right = (self.lowestCommonAncestor(kid, p, q) for kid in (root.left, root.right))
        return root if left and right else left or right

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

# 270. Closest Binary Search Tree Value
# Given the root of a binary search tree and a target value, return the value in the BST that is closest to the target. If there are multiple answers, print the smallest.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Closest_Binary_Search_Tree_Value:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        min_diff = sys.maxsize
        min_val = -1
        def dfs(node):
            nonlocal min_diff, min_val
            if node is None: return
            if abs(target - node.val) < min_diff:
                min_diff = abs(target - node.val)
                min_val = node.val
            elif abs(target - node.val) == min_diff:
                if node.val < min_val:
                    min_val = node.val
            if node.val > target:
                dfs(node.left)
            else:
                dfs(node.right)
        dfs(root)
        return min_val

# 543. Diameter of Binary Tree
# Given the root of a binary tree, return the length of the diameter of the tree.
#
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
#
# The length of a path between two nodes is represented by the number of edges between them.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Diameter_of_Binary_Tree:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def longest_path(node):
            if not node: return 0
            nonlocal diameter

            left_path, right_path = longest_path(node.left), longest_path(node.right)

            diameter = max(diameter, left_path + right_path)

            return max(left_path, right_path) + 1

        longest_path(root)
        return diameter

# 173. Binary Search Tree Iterator
# Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):
#
# BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
# boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
# int next() Moves the pointer to the right, then returns the number at the pointer.
# Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.
#
# You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order traversal when next() is called.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.traverse = []

        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            self.traverse.append(node)
            dfs(node.right)

        dfs(root)
        self.index = -1

    def next(self) -> int:
        self.index += 1
        return self.traverse[self.index].val

    def hasNext(self) -> bool:
        return self.index + 1 < len(self.traverse)

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

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