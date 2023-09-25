from DFS import RemoveInvalidParenthesis
from backtrack import WordPattern
from linkedList import LinkedList, ListNode
from dynamic_programming import WordBreakII
s = "catsanddog"
wordDict = ["cat","cats","and","sand","dog"]
wb2 = WordBreakII()
output = wb2.wordBreak_iter(wordDict=wordDict, s=s)
output2 = wb2.wordBreak_rec(wordDict=wordDict, s=s)
print(output)
# input = [1,4,3,2,5,2]
# x = 3
# #Output: [1,2,2,4,3,5]
# head = ListNode(input[0])
# walker = head
# for val in input[1:]:
#   walker.next = ListNode(val)
#   walker = walker.next
# ll = LinkedList()
# par = ll.partition(head, 3)
# print(par)
# input = [1,2,3,4,5]
# head = ListNode(input[0])
# walker = head
# for val in input[1:]:
#   walker.next = ListNode(val)
#   walker = walker.next
# ll = LinkedList()
# revLL = ll.reverseList(head)
# print(revLL)


# wp1 = WordPattern()
# pattern = "abab"
# str = "redblueredblue"
# print(f"solution = {wp1.backtrack(pattern, str, {})}")


# rip = RemoveInvalidParenthesis()
# '''
# Example 1:
#
# Input: s = "()())()"
# Output: ["(())()","()()()"]
# Example 2:
#
# Input: s = "(a)())()"
# Output: ["(a())()","(a)()()"]
# Example 3:
#
# Input: s = ")("
# Output: [""]
# '''
# s = "()())()"
# print(rip.remove_invalid_parentheses(s))

