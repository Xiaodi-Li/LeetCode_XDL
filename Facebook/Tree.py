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