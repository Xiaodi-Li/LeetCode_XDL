'''
1. Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
'''
from typing import List
from collections import defaultdict
class SumSeries:
  def twoSum_2run(self, nums: List[int], target: int) -> List[int]:
    val_dict = defaultdict(int)
    for i, num in enumerate(nums):
      if num not in val_dict:
        val_dict[num] = i
    for i, num in enumerate(nums):
      if target - num in val_dict and i != val_dict[target - num]:
        return i, val_dict[target - num]
  def twoSum_1run(self, nums: List[int], target: int) -> List[int]:
    hash_set = {}
    for i, num in enumerate(nums):
      if target - num in hash_set and hash_set[target - num] != i:
        return [i, hash_set[target - num]]
      hash_set[num] = i
  '''
  15 3sum
  Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
  Notice that the solution set must not contain duplicate triplets.
  '''
  def threeSum(self, nums: List[int]) -> List[List[int]]:
    nums.sort()
    output = set()
    for i, num in enumerate(nums):
      j, k = i + 1, len(nums) - 1
      while j < k:
        if nums[j] + nums[k] == -num:
          output.add((num, nums[j], nums[k]))
          j += 1
          k -= 1
        elif nums[j] + nums[k] < -num:
          j += 1
        else:
          k -= 1
    return output
  '''
  3sum variations with a^2 + b^2 = c^2 (2)?
  '''
  def threeSumSquared(self, nums):
    # First, let's square each number and sort the list
    nums = sorted([x ** 2 for x in nums])
    res = []
    n = len(nums)
    for i in range(n - 1, 1, -1): # Let's use c as our third number
      c = nums[i]
      l, r = 0, i - 1 # Now, we'll use two pointers to find a and b
      while l < r:
        if nums[l] + nums[r] == c:
          a = int(nums[l] ** 0.5)
          b = int(nums[r] ** 0.5)
          c_sqrt = int(c ** 0.5)
          res.append([a, b, c_sqrt])
          l += 1
          r -= 1
        elif nums[l] + nums[r] < c:
          l += 1
        else:
          r -= 1
    return res
# 523. Continuous Subarray Sum
# Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.
# A good subarray is a subarray where:
# its length is at least two, and
# the sum of the elements of the subarray is a multiple of k.
# Note that:
# A subarray is a contiguous part of the array.
# An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.
'''
Example 1:

Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
Example 2:

Input: nums = [23,2,6,4,7], k = 6
Output: true
Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.
Example 3:
Input: nums = [23,2,6,4,7], k = 13
Output: false
		# example - [23,2,6,4,7]
        # [[23,1]]
        # [[25,2], [2,1]]
        # [[31,3], [8,2], [6,1]]
        # [[35,4], [12,3], [10,2], [4,1]] <-- found 12
        ##the following approach makes uses of the property that when mod appear second time, there must be a k a
'''
class Continuous_Subarray_Sum:
  def checkSubarraySum(self, nums: List[int], k: int) -> bool:
    remainder = {0: -1}
    total = 0
    for i, num in enumerate(nums):
      total += num
      r = total % k
      if r not in remainder:
        remainder[r] = i
      elif i - remainder[r] > 1:
        return True
    return False