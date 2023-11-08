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

# 921. Minimum Add to Make Parentheses Valid
# A parentheses string is valid if and only if:
#
# It is the empty string,
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.
# You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.
#
# For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".
# Return the minimum number of moves required to make s valid.
class Minimum_Add:
    def minAddToMakeValid(self, s: str) -> int:
        ans = bal = 0
        for ch in s:
            bal += 1 if ch == '(' else -1
            if bal == -1:
                ans += 1
                bal += 1
        return ans + bal

# 415. Add Strings
# Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.
#
# You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.
class Add_Strings:
    def addStrings(self, num1: str, num2: str) -> str:
        res = []
        carry = 0

        p1, p2 = len(num1) - 1, len(num2) - 1
        while p1 >= 0 or p2 >= 0:
            x1 = ord(num1[p1]) - ord('0') if p1 >= 0 else 0
            x2 = ord(num2[p2]) - ord('0') if p2 >= 0 else 0
            value = (x1 + x2 + carry) % 10
            carry = (x1 + x2 + carry) // 10

            res.append(value)
            p1 -= 1
            p2 -= 1

        if carry:
            res.append(carry)

        return ''.join(str(x) for x in res[::-1])

# 953. Verifying an Alien Dictionary
# In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.
#
# Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.
class Verifying_an_Alien_Dictionary:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_dict = {char: i for i, char in enumerate(order)}
        for i in range(len(words) - 1):
            for j in range(len(words[i])):
                if j > len(words[i + 1]) - 1:
                    return False
                if order_dict[words[i][j]] > order_dict[words[i + 1][j]]:
                    return False
                if order_dict[words[i][j]] < order_dict[words[i + 1][j]]:
                    break
        return True

# 125. Valid Palindrome
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
#
# Given a string s, return true if it is a palindrome, or false otherwise.
class Valid_Palindrome:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = ''.join(filter(str.isalnum, s))

        for i in range(len(s) // 2):
            if s[i] == s[len(s) - i - 1]:
                continue
            else:
                return False
        return True

# 140. Word Break II
# Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.
#
# Note that the same word in the dictionary may be reused multiple times in the segmentation.
class Word_Break_II:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words = set(wordDict)
        mem = {}

        def wordbreak(s):
            if s in mem: return mem[s]
            ans = []
            if s in words: ans.append(s)

            for i in range(1, len(s)):
                right = s[i:]
                if right not in words: continue
                ans += [w + ' ' + right for w in wordbreak(s[:i])]
            mem[s] = ans
            return mem[s]

        return wordbreak(s)

# 1541. Minimum Insertions to Balance a Parentheses String
# Given a parentheses string s containing only the characters '(' and ')'. A parentheses string is balanced if:
#
# Any left parenthesis '(' must have a corresponding two consecutive right parenthesis '))'.
# Left parenthesis '(' must go before the corresponding two consecutive right parenthesis '))'.
# In other words, we treat '(' as an opening parenthesis and '))' as a closing parenthesis.
#
# For example, "())", "())(())))" and "(())())))" are balanced, ")()", "()))" and "(()))" are not balanced.
# You can insert the characters '(' and ')' at any position of the string to balance it if needed.
#
# Return the minimum number of insertions needed to make s balanced.
class Minimum_Insertions_BPS:
    def minInsertions(self, s: str) -> int:
        res = right = 0
        for c in s:
            if c == '(':
                if right % 2:
                    right -= 1
                    res += 1
                right += 2
            if c == ')':
                right -= 1
                if right < 0:
                    right += 2
                    res += 1
        return res + right

'''
"(()))"
right: 0, 2, 4, 3, 2, 1 
res:   0, 0, 0, 0, 0, 0

"))())("
right: 0, 1, 0, 2, 1, 0, 2  
res:   0, 1, 1, 1, 1, 1, 1
'''

# 38. Count and Say
# The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
#
# countAndSay(1) = "1"
# countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.
# To determine how you "say" a digit string, split it into the minimal number of substrings such that each substring contains exactly one unique digit. Then for each substring, say the number of digits, then say the digit. Finally, concatenate every said digit.
#
# For example, the saying and conversion for digit string "3322251":
class Count_and_Say:
    def countAndSay(self, n: int) -> str:
        prev = '1'

        for _ in range(n - 1):
            new = ''
            count = 1
            for i in range(1, len(prev)):
                if prev[i] == prev[i - 1]:
                    count += 1
                else:
                    new += str(count) + prev[i - 1]
                    count = 1
            new += str(count) + prev[-1]
            prev = new

        return prev

# 1209. Remove All Adjacent Duplicates in String II
# You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them, causing the left and the right side of the deleted substring to concatenate together.
#
# We repeatedly make k duplicate removals on s until we no longer can.
#
# Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.
class Remove_All_Adjacent_Duplicates_in_String_II:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for c in s:
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1
            else:
                stack.append([c, 1])
            if stack[-1][1] == k:
                stack.pop()
        res = ""
        for char, count in stack:
            res += (char * count)
        return res

# 1060. Missing Element in Sorted Array
# Given an integer array nums which is sorted in ascending order and all of its elements are unique and given also an integer k, return the kth missing number starting from the leftmost number of the array.
class Missing_Element_in_Sorted_Array:
    def missingElement(self, nums: List[int], k: int) -> int:
        for i in range(1, len(nums)):
            missing_count = nums[i] - nums[i - 1] - 1
            if k <= missing_count:
                return nums[i - 1] + k
            k -= missing_count
        return nums[-1] + k

'''
[4,7,9,10]
k = 3
missing_count: 2, 1 
k:             1, 1 return 8

[1,2,4]
k = 3
missing_count: 0, 1, 
k:             3, 2, return 6
'''