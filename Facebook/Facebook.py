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
