'''
341. Flatten Nested List Iterator
You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists. Implement an iterator to flatten it.

Implement the NestedIterator class:

NestedIterator(List<NestedInteger> nestedList) Initializes the iterator with the nested list nestedList.
int next() Returns the next integer in the nested list.
boolean hasNext() Returns true if there are still some integers in the nested list and false otherwise.
Your code will be tested with the following pseudocode:

initialize iterator with nestedList
res = []
while iterator.hasNext()
    append iterator.next() to the end of res
return res
If res matches the expected flattened list, then your code will be judged as correct.



Example 1:

Input: nestedList = [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].
Example 2:

Input: nestedList = [1,[4,[6]]]
Output: [1,4,6]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].
'''
from typing import List

'''
498. Diagonal Traverse
Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.
Example 1:
Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]
Example 2:
Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]
'''
from collections import defaultdict
class DiagonalTravasal:
  def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
    '''
    we have m+n-1 rows, starting from 1 to m, increasing num of each row,
    after that, lower from m or m-1 to 1, depending on m+n-1 is odd or even,
    starting from second row, we have left rise, right fall, then, left fall, right rise pattern
    time complexity: O(N⋅M)
    space complexity: O(min(N, M))
    '''
    if not matrix or not matrix[0]: return None
    N, M = len(matrix), len(matrix[0])
    result, intermediate = [], []
    for d in range(N + M - 1):
      intermediate.clear()
      r, c = 0 if d < M else d - M + 1, d if d < M else M - 1
      while r < N and c > -1:
        intermediate.append(matrix[r][c])
        r += 1
        c -= 1
      if d % 2 == 0:
        result.extend(intermediate[::-1])
      else:
        result.extend(intermediate)
    return result

  def findDiagonalOrder_dict(self, matrix: List[List[int]]) -> List[int]:
    '''
    we have m+n-1 rows, starting from 1 to m, increasing num of each row,
    after that, lower from m or m-1 to 1, depending on m+n-1 is odd or even,
    starting from second row, we have left rise, right fall, then, left fall, right rise pattern
    time complexity: O(N⋅M)
    space complexity: O(min(N, M))
    '''
    if not matrix or not matrix[0]: return None
    diag_hm = defaultdict(list)
    m, n = len(matrix), len(matrix[0])
    for i in range(m):
      for j in range(n):
        diag_hm[i + j].append(matrix[i][j])
    ans = []
    for ij in diag_hm.keys():
      if ij % 2 == 0:
        ans.extend(diag_hm[ij][::-1])
      else:
        ans.extend(diag_hm[ij])
    return ans
# class NestedIterator:
#   def __init__(self, nestedList: [NestedInteger]):
#     self.stack = []
#     # Add the nestedList to the stack in reverse order
#     for i in range(len(nestedList) - 1, -1, -1):
#       self.stack.append(nestedList[i])
#
#   def next(self) -> int:
#     return self.stack.pop().getInteger()
#
#   def hasNext(self) -> bool:
#     # Flatten the list by popping elements from the stack until we find an integer
#     while self.stack:
#       current = self.stack[-1]
#       if current.isInteger():
#         return True
#
#       # If it's a list, pop it and push its elements in reverse order
#       self.stack.pop()
#       nested_list = current.getList()
#       for i in range(len(nested_list) - 1, -1, -1):
#         self.stack.append(nested_list[i])
#
#     return False
#
# class NestedIteratorRec:
#   def __init__(self, nestedList):
#     self.stack = []
#     self.flatten(nestedList)
#
#   def flatten(self, nestedList):
#     for item in reversed(nestedList):
#       if item.isInteger():
#         self.stack.append(item.getInteger())
#       else:
#         self.flatten(item.getList())
#
#   def next(self):
#     return self.stack.pop()
#
#   def hasNext(self):
#     return len(self.stack) > 0
#
#
#   def flat(self, arr, n):
#     ans = []
#     def dfs(depth, maxDepth, currArray):
#       if depth == maxDepth:
#         ans.append(currArray)
#         return
#       for element in currArray:
#         if isinstance(element, list):
#           dfs(depth + 1, maxDepth, element)
#         else:
#           ans.append(element)
#     dfs(-1, n, arr)
#     return ans
#
