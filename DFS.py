# 780 · Remove Invalid Parentheses
# Description
# Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.
from typing import (
    List,
)

class Solution:
    """
    @param s: The input string
    @return: Return all possible results
             we will sort your return value in output
    """
    def remove_invalid_parentheses(self, s: str) -> List[str]:
        # Write your code here
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
                
                if s[i] == '(' or s[i] == ')':
                    curr = s[:i] + s[i + 1:]
                    if r > 0 and s[i] == ')':
                        dfs(curr, i, l, r - 1, ans)
                    elif l > 0 and s[i] == '(':
                        dfs(curr, i, l - 1, r, ans)
            
        l = 0
        r = 0

        for ch in s:
            l += (ch == '(')
            if l == 0:
                r += (ch == ')')
            else:
                l -= (ch == ')')
        
        ans = []
        dfs(s, 0, l, r, ans)
        return ans  

# 829 · Word Pattern II
# Description
# Given a pattern and a string str, find if str follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty substring in str.(i.e if a corresponds to s, then b cannot correspond to s. For example, given pattern = "ab", str = "ss", return false.)
# Solution 1
class WordPattern_1:
    def wordPatternMatch(self, pattern, string):
        return self.match(pattern, string, {}, set())

    def match(self, pattern, string, dict, used):
        if not pattern:
            return not string

        ch = pattern[0]

        if ch in dict:
            word = dict[ch]
            if not string.startswith(word):
                return False
            return self.match(pattern[1:], string[len(word):], dict, used)

        for i in range(len(string)):
            word = string[:i + 1]
            if word in used:
                continue

            dict[ch] = word
            used.add(word)

            if self.match(pattern[1:], string[i + 1:], dict, used):
                return True

            used.remove(word)
            del dict[ch]

        return False

# Solution 2
class WordPattern_2:
    def wordPatternMatch(self, pattern, str):
        map = {}
        return self.dfs(pattern, str, map)

    def dfs(self, ptn, s, map):
        if len(ptn) == 0 and len(s) == 0:
            return True

        if len(ptn) == 0 or len(s) == 0:
            return False

        if ptn[0] in map:
            prefix = map[ptn[0]]
            if not s.startswith(prefix):
                return False
            return self.dfs(ptn[1:], s[len(prefix):], map)

        for i in range(1, len(s) + 1):
            prefix = s[:i]
            if prefix in map.values():
                continue
            map[ptn[0]] = prefix
            if self.dfs(ptn[1:], s[len(prefix):], map):
                return True
            del map[ptn[0]]

        return False

# 34 · N-Queens II
# Description
# According to N-Queens problem.
#
# Now, instead outputting board configurations, return the total number of distinct solutions.
class N_Queens_II:
    """
    @param n: The number of queens.
    @return: The total number of distinct solutions.
    """

    def total_n_queens(self, n: int) -> int:
        # write your code here
        col = set()
        pos_diag = set()
        neg_diag = set()
        self.res = 0

        def backtracking(r):
            if r == n:
                self.res += 1
                return

            for c in range(n):
                if c in col or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue

                col.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)

                backtracking(r + 1)

                col.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)

        backtracking(0)
        return self.res

# 152 · Combinations
# Description
# Given two integers n and k. Return all possible combinations of k numbers out of 1, 2, ... , n.
class Combinations:
    """
    @param n: Given the range of numbers
    @param k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n
             we will sort your return value in output
    """

    def combine(self, n: int, k: int) -> List[List[int]]:
        # write your code here
        self.results = []

        nums = []
        for i in range(1, n + 1):
            nums.append(i)

        self.dfs(nums, k, [], 0)

        return self.results

    def dfs(self, nums, k, subset, index):
        if len(subset) == k:
            self.results.append(subset)
            return

        for i in range(index, len(nums)):
            self.dfs(nums, k, subset + [nums[i]], i + 1)

# 153 · Combination Sum II
# Description
# Given an array num and a number target. Find all unique combinations in num where the numbers sum to target.
class Combination_Sum_II:
    """
    @param num: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
             we will sort your return value in output
    """

    def combination_sum2(self, num: List[int], target: int) -> List[List[int]]:
        # write your code here
        num.sort()

        res = []

        def backtrack(cur, pos, target):
            if target == 0:
                res.append(cur.copy())
            if target <= 0:
                return

            prev = -1
            for i in range(pos, len(num)):
                if num[i] == prev:
                    continue

                cur.append(num[i])
                backtrack(cur, i + 1, target - num[i])
                cur.pop()
                prev = num[i]

        backtrack([], 0, target)
        return res


