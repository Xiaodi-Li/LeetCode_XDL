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
