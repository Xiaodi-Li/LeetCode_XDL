# 17. Letter Combinations of a Phone Number
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
#
# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
class Letter_Combinations_of_a_Phone_Number:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        ans = ['']
        d = [' ', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

        for digit in digits:
            tmp = []
            for s in ans:
                for c in d[ord(digit) - ord('0')]:
                    tmp.append(s + c)
            ans = tmp

        return ans