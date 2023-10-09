# 1. Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.
class Two_Sum:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            if target - nums[i] in hashmap and i != hashmap[target - nums[i]]:
                return [i, hashmap[target - nums[i]]]
            hashmap[nums[i]] = i

# 2. Add Two Numbers
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Add_Two_Numbers:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy

        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)

            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next

# 3. Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest
# substring
#  without repeating characters.
class Longest_Substring_Without:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, len(charSet))

        return res

# 4. Median of Two Sorted Arrays
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
#
# The overall run time complexity should be O(log (m+n)).
class Median_of_Two:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(A) > len(B):
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2

            Aleft = A[i] if i >= 0 else float('-inf')
            Aright = A[i + 1] if i + 1 < len(A) else float('inf')
            Bleft = B[j] if j >= 0 else float('-inf')
            Bright = B[j + 1] if j + 1 < len(B) else float('inf')

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1

# 5. Longest Palindromic Substring
# Given a string s, return the longest palindromic substring in s.
class Longest_Palindromic_Substring:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > resLen:
                    res = s[l:r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1

            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > resLen:
                    res = s[l:r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1

        return res

# 6. Zigzag Conversion
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
#
# Write the code that will take a string and make this conversion given a number of rows:
#
# string convert(string s, int numRows);
class Zigzag_Conversion:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        res = ""

        for r in range(numRows):
            increment = 2 * (numRows - 1)
            for i in range(r, len(s), increment):
                res += s[i]
                if 0 < r < numRows - 1 and i + increment - 2 * r < len(s):
                    res += s[i + increment - 2 * r]

        return res

# 7. Reverse Integer
# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
#
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
class Reverse_Integer:
    def reverse(self, x: int) -> int:
        MIN = - 2 ** 31
        MAX = 2 ** 31 - 1

        res = 0
        while x:
            digit = int(math.fmod(x, 10))
            x = int(x / 10)

            if res > MAX // 10 or (res == MAX // 10 and digit > MAX % 10):
                return 0
            if res < MIN // 10 or (res == MIN // 10 and digit < MIN % 10):
                return 0

            res = res * 10 + digit

        return res

# 8. String to Integer (atoi)
# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).
#
# The algorithm for myAtoi(string s) is as follows:
#
# Read in and ignore any leading whitespace.
# Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
# Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
# Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
# If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
# Return the integer as the final result.
# Note:
#
# Only the space character ' ' is considered a whitespace character.
# Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.
class String_to_Integer:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        negative = False
        out = 0

        if s[0] == '-':
            negative = True
        elif s[0] == '+':
            negative = False
        elif not s[0].isnumeric():
            return 0
        else:
            out = ord(s[0]) - ord('0')

        for i in range(1, len(s)):
            if s[i].isnumeric():
                out = out * 10 + ord(s[i]) - ord('0')
                if not negative and out >= 2 ** 31 - 1:
                    return 2 ** 31 - 1
                if negative and out >= 2 ** 31:
                    return - 2 ** 31
            else:
                break

        if negative:
            return - out
        else:
            return out

# 9. Palindrome Number
# Given an integer x, return true if x is a
# palindrome
# , and false otherwise.
class Palindrome_Number:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        reverse_num = 0
        temp = x

        while temp:
            digit = temp % 10
            reverse_num = reverse_num * 10 + digit
            temp //= 10

        return reverse_num == x

# 10. Regular Expression Matching
# Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:
#
# '.' Matches any single character.​​​​
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).
class Regular_Expression_Matching:
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def dfs(i, j):
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False

            match = i < len(s) and (s[i] == p[j] or p[j] == '.')
            if j + 1 < len(p) and p[j + 1] == '*':
                return dfs(i, j + 2) or (match and dfs(i + 1, j))
            if match:
                return dfs(i + 1, j + 1)

            return False

        return dfs(0, 0)

# 314. Binary Tree Vertical Order Traversal
#
# Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).
#
# If two nodes are in the same row and column, the order should be from left to right.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Binary_Tree_V:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        cols = collections.defaultdict(list)
        queue = [(root, 0)]

        for node, i in queue:
            if node:
                cols[i].append(node.val)
                queue += (node.left, i - 1), (node.right, i + 1)

        return [cols[i] for i in sorted(cols)]

# 408. Valid Word Abbreviation
# A string can be abbreviated by replacing any number of non-adjacent, non-empty substrings with their lengths. The lengths should not have leading zeros.
#
# For example, a string such as "substitution" could be abbreviated as (but not limited to):
#
# "s10n" ("s ubstitutio n")
# "sub4u4" ("sub stit u tion")
# "12" ("substitution")
# "su3i1u2on" ("su bst i t u ti on")
# "substitution" (no substrings replaced)
# The following are not valid abbreviations:
#
# "s55n" ("s ubsti tutio n", the replaced substrings are adjacent)
# "s010n" (has leading zeros)
# "s0ubstitution" (replaces an empty substring)
# Given a string word and an abbreviation abbr, return whether the string matches the given abbreviation.
#
# A substring is a contiguous non-empty sequence of characters within a string.
class Valid_Word_Abbr:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = j = 0
        m, n = len(word), len(abbr)

        while i < m and j < n:
            if word[i] == abbr[j]:
                i += 1
                j += 1
            elif abbr[j] == '0':
                return False
            elif abbr[j].isnumeric():
                k = j
                while k < n and abbr[k].isnumeric():
                    k += 1
                i += int(abbr[j:k])
                j = k
            else:
                return False

        return i == m and j == n

# 1762. Buildings With an Ocean View
# There are n buildings in a line. You are given an integer array heights of size n that represents the heights of the buildings in the line.
#
# The ocean is to the right of the buildings. A building has an ocean view if the building can see the ocean without obstructions. Formally, a building has an ocean view if all the buildings to its right have a smaller height.
#
# Return a list of indices (0-indexed) of buildings that have an ocean view, sorted in increasing order.
class Ocean_View:
    def findBuildings(self, heights: List[int]) -> List[int]:
        rev_heights = heights[::-1]
        max_height = 0
        res = []

        for i in range(len(heights)):
            if rev_heights[i] > max_height:
                res.append(len(heights) - i - 1)
            max_height = max(max_height, rev_heights[i])
        res = res[::-1]

        return res

# 1249. Minimum Remove to Make Valid Parentheses
# Given a string s of '(' , ')' and lowercase English characters.
#
# Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.
#
# Formally, a parentheses string is valid if and only if:
#
# It is the empty string, contains only lowercase characters, or
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.
class Minimum_Remove_Valid_Parentheses:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        split_str = list(s)

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if len(stack) != 0:
                    stack.pop()
                else:
                    split_str[i] = ''

        for i in stack:
            split_str[i] = ''

        return ''.join(split_str)

# 680. Valid Palindrome II
# Given a string s, return true if the s can be palindrome after deleting at most one character from it.
class Valid_Palindrome_II:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                skipL, skipR = s[l + 1:r + 1], s[l:r]
                return skipL == skipL[::-1] or skipR == skipR[::-1]
            l += 1
            r -= 1

        return True

# 1570. Dot Product of Two Sparse Vectors
#
# Given two sparse vectors, compute their dot product.
#
# Implement class SparseVector:
#
# SparseVector(nums) Initializes the object with the vector nums
# dotProduct(vec) Compute the dot product between the instance of SparseVector and vec
# A sparse vector is a vector that has mostly zero values, you should store the sparse vector efficiently and compute the dot product between two SparseVector.
#
# Follow up: What if only one of the vectors is sparse?
class SparseVector:
    def __init__(self, nums: List[int]):
        self.seen = {}
        for i, n in enumerate(nums):
            if n != 0:
                self.seen[i] = n

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        for j, n in vec.seen.items():
            if j in self.seen:
                res += n * self.seen[j]
        return res

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)

# 528. Random Pick with Weight
class Random_Pick:

    def __init__(self, w: List[int]):
        self.prefix_sums = []
        prefix_sum = 0
        for w_i in w:
            prefix_sum += w_i
            self.prefix_sums.append(prefix_sum)
        self.total_sum = prefix_sum

    def pickIndex(self) -> int:
        target = self.total_sum * random.random()
        left, right = 0, len(self.prefix_sums)
        while left < right:
            mid = (left + right) // 2
            if target > self.prefix_sums[mid]:
                left = mid + 1
            else:
                right = mid
        return left

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

# 1650. Lowest Common Ancestor of a Binary Tree III
# Given two nodes of a binary tree p and q, return their lowest common ancestor (LCA).
#
# Each node will have a reference to its parent node. The definition for Node is below:
#
# class Node {
#     public int val;
#     public Node left;
#     public Node right;
#     public Node parent;
# }
# According to the definition of LCA on Wikipedia: "The lowest common ancestor of two nodes p and q in a tree T is the lowest node that has both p and q as descendants (where we allow a node to be a descendant of itself)."
"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""


class Lowest_Common_Ancestor_II:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p1, p2 = p, q

        while p1 != p2:
            p1 = p1.parent if p1.parent else q
            p2 = p2.parent if p2.parent else p

        return p1

# 227. Basic Calculator II
# Given a string s which represents an expression, evaluate this expression and return its value.
#
# The integer division should truncate toward zero.
#
# You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].
#
# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().
class Basic_Calculator_II:
    def calculate(self, s: str) -> int:
        def update(op, v):
            if op == '+': stack.append(v)
            if op == '-': stack.append(-v)
            if op == '*': stack.append(stack.pop() * v)
            if op == '/': stack.append(int(stack.pop() / v))

        it, num, stack, sign = 0, 0, [], '+'

        while it < len(s):
            if s[it].isnumeric():
                num = num * 10 + int(s[it])
            elif s[it] in '+-/*':
                update(sign, num)
                num, sign = 0, s[it]
            elif s[it] == '(':
                num, j = self.calculate(s[it + 1:])
                it = it + j
            elif s[it] == ')':
                update(sign, num)
                return sum(stack), it + 1
            it += 1

        update(sign, num)
        return sum(stack)

# 339. Nested List Weight Sum
# You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists.
#
# The depth of an integer is the number of lists that it is inside of. For example, the nested list [1,[2,2],[[3],2],1] has each integer's value set to its depth.
#
# Return the sum of each integer in nestedList multiplied by its depth.
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Nested_List_Weight_Sum:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:

        def dfs(nested_list, depth):
            total = 0
            for nested in nested_list:
                if nested.isInteger():
                    total += nested.getInteger() * depth
                else:
                    total += dfs(nested.getList(), depth + 1)
            return total

        return dfs(nestedList, 1)

# 215. Kth Largest Element in an Array
# Given an integer array nums and an integer k, return the kth largest element in the array.
#
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
#
# Can you solve it without sorting?
class Kth_Largest_Element:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)

        for num in nums[k:]:
            if num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)

        return heap[0]

# 71. Simplify Path
# Given a string path, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style file system, convert it to the simplified canonical path.
#
# In a Unix-style file system, a period '.' refers to the current directory, a double period '..' refers to the directory up a level, and any multiple consecutive slashes (i.e. '//') are treated as a single slash '/'. For this problem, any other format of periods such as '...' are treated as file/directory names.
#
# The canonical path should have the following format:
#
# The path starts with a single slash '/'.
# Any two directories are separated by a single slash '/'.
# The path does not end with a trailing '/'.
# The path only contains the directories on the path from the root directory to the target file or directory (i.e., no period '.' or double period '..')
# Return the simplified canonical path.
class Simplify_Path:
    def simplifyPath(self, path: str) -> str:
        stack = []
        cur = ''

        for c in path + '/':
            if c == '/':
                if cur == '..':
                    if stack: stack.pop()
                elif cur != '' and cur != '.':
                    stack.append(cur)
                cur = ''
            else:
                cur += c

        return '/' + '/'.join(stack)

# 249. Group Shifted Strings
# We can shift a string by shifting each of its letters to its successive letter.
#
# For example, "abc" can be shifted to be "bcd".
# We can keep shifting the string to form a sequence.
#
# For example, we can keep shifting "abc" to form the sequence: "abc" -> "bcd" -> ... -> "xyz".
# Given an array of strings strings, group all strings[i] that belong to the same shifting sequence. You may return the answer in any order.
class Group_Shifted_Strings:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        hashmap = {}

        for s in strings:
            key = ()
            for i in range(len(s) - 1):
                circular_difference = 26 + ord(s[i + 1]) - ord(s[i])
                key += (circular_difference % 26,)
            hashmap[key] = hashmap.get(key, []) + [s]

        return list(hashmap.values())

# 791. Custom Sort String
# You are given two strings order and s. All the characters of order are unique and were sorted in some custom order previously.
#
# Permute the characters of s so that they match the order that order was sorted. More specifically, if a character x occurs before a character y in order, then x should occur before y in the permuted string.
#
# Return any permutation of s that satisfies this property.
class Custom_Sort_String:
    def customSortString(self, order: str, s: str) -> str:
        count = collections.Counter(s)
        ans = []

        for c in order:
            if c in count:
                ans.append(c * count[c])

            count[c] = 0

        for c in count:
            ans.append(c * count[c])

        return ''.join(ans)








