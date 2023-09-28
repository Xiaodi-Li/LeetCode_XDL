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

# 426 · Restore IP Addresses
# Description
# Given a string containing only digits, restore it by returning all possible valid IP address combinations.
#
# (Your task is to add three dots to this string to make it a valid IP address. Return all possible IP address.)
class Restore_IP:
    """
    @param s: the IP string
    @return: All possible valid IP addresses
             we will sort your return value in output
    """

    def restore_ip_addresses(self, s: str) -> List[str]:
        # write your code here
        res = []

        if len(s) > 12:
            return res

        def backtrack(i, dots, curIP):
            if dots == 4 and i == len(s):
                res.append(curIP[:-1])
                return
            if dots > 4:
                return

            for j in range(i, min(i + 3, len(s))):
                if int(s[i:j + 1]) < 256 and (i == j or s[i] != '0'):
                    backtrack(j + 1, dots + 1, curIP + s[i:j + 1] + '.')

        backtrack(0, 0, '')
        return res

# 570 · Find the Missing Number II
# Description
# Given a permutation of 1 - n integers in random order, find an integer that is missing.
class Missing_Number_II:
    """
    @param n: An integer
    @param s: a string with number from 1-n in random order and miss one number
    @return: An integer
    """

    def find_missing2(self, n: int, s: str) -> int:
        # write your code here
        self.theMissing = -1
        isFound = [False] * (n + 1)
        self.dfs(n, s, 0, isFound)
        return self.theMissing

    def dfs(self, n, s, start, isFound):
        if self.theMissing != -1:
            return

        if start == len(s):
            for i in range(1, n + 1):
                if not isFound[i]:
                    self.theMissing = i
                    return
            return

        if s[start] == '0':
            return

        for ch in range(1, 3):
            if start + ch <= len(s):
                num = int(s[start:start + ch])
                if 0 < num <= n and not isFound[num]:
                    isFound[num] = True
                    self.dfs(n, s, start + ch, isFound)
                    isFound[num] = False

# 680 · Split String
# Description
# Give a string, you can choose to split the string after one character or two adjacent characters, and make the string to be composed of only one character or two characters. Output all possible results.
class Split_String:
    """
    @param s: a string to be split
    @return: all possible split string array
    """

    def split_string(self, s: str) -> List[List[str]]:
        # write your code here
        res = []
        self.dfs(res, [], s)
        return res

    def dfs(self, res, path, s):
        if s == "":
            res.append(path[:])
            return

        for i in range(2):
            if i + 1 <= len(s):
                path.append(s[:i + 1])
                self.dfs(res, path, s[i + 1:])
                path.pop()

# 780 · Remove Invalid Parentheses
# Description
# Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.
class Invalid_Parentheses:
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
                    if l > 0 and s[i] == '(':
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

# 802 · Sudoku Solver
# Description
# Write a program to solve a Sudoku puzzle by filling the empty cells.
#
# Empty cells are indicated by the number 0.
#
# You may assume that there will be only one unique solution.
class Sudoku:
    """
    @param board: the sudoku puzzle
    @return: nothing
    """

    def solve_sudoku(self, board: List[List[int]]):
        # write your code here
        self.backtrack(board, 0, 0)
        return board

    def backtrack(self, board, i, j):
        m, n = 9, 9
        if j == n:
            return self.backtrack(board, i + 1, 0)
        if i == m:
            return True
        if board[i][j] != 0:
            return self.backtrack(board, i, j + 1)
        for val in range(1, 10):
            if not self.isValid(board, i, j, val):
                continue
            board[i][j] = val
            if self.backtrack(board, i, j):
                return True
            board[i][j] = 0

    def isValid(self, board, row, col, val):
        for i in range(9):
            if board[row][i] == val:
                return False
            if board[i][col] == val:
                return False
            if board[row // 3 * 3 + i // 3][col // 3 * 3 + i % 3] == val:
                return False
        return True

# 816 · Traveling Salesman Problem
# Description
# Give n cities(labeled from 1 to n), and the undirected road's cost among the cities as a three-tuple [A, B, c](i.e there is a road between city A and city B and the cost is c). We need to find the smallest cost to travel all the cities starting from 1.
class Traveling_Salesman:
    """
    @param n: an integer,denote the number of cities
    @param roads: a list of three-tuples,denote the road between cities
    @return: return the minimum cost to travel all cities
    """

    def min_cost(self, n: int, roads: List[List[int]]) -> int:
        # Write your code here
        self.n = n
        self.g = [[float('inf')] * n for _ in range(n)]
        self.done = [False] * n
        self.res = float('inf')

        for x, y, c in roads:
            x -= 1
            y -= 1
            self.g[x][y] = min(self.g[x][y], c)
            self.g[y][x] = min(self.g[y][x], c)

        self.done[0] = True
        self.dfs(1, 0, 0)
        return self.res

    def dfs(self, level, p, c):
        if c >= self.res:
            return

        if level == self.n:
            self.res = c
            return

        for i in range(self.n):
            if not self.done[i] and self.g[p][i] != float('inf'):
                self.done[i] = True
                self.dfs(level + 1, i, c + self.g[p][i])
                self.done[i] = False

# 829 · Word Pattern II
# Description
# Given a pattern and a string str, find if str follows the same pattern.
#
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty substring in str.(i.e if a corresponds to s, then b cannot correspond to s. For example, given pattern = "ab", str = "ss", return false.)
class Word_Pattern_II:
    """
    @param pattern: a string,denote pattern string
    @param str: a string, denote matching string
    @return: a boolean
    """

    def word_pattern_match(self, pattern: str, str: str) -> bool:
        # write your code here
        return self.backtrack(pattern, str, {})

    def backtrack(self, ptn, s, map):
        if not ptn: return not s

        if ptn[0] in map:
            prefix = map[ptn[0]]
            if not s.startswith(prefix): return False
            return self.backtrack(ptn[1:], s[len(prefix):], map)

        for i in range(1, len(s) + 1):
            prefix = s[:i]
            if prefix in map.values(): continue
            map[ptn[0]] = prefix
            if self.backtrack(ptn[1:], s[len(prefix):], map): return True
            del map[ptn[0]]

        return False