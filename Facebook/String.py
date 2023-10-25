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
