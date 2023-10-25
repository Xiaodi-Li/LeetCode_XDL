# 56. Merge Intervals
# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
class Merge_Intervals:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        i = 0
        while i < len(intervals) - 1:
            if intervals[i][1] >= intervals[i + 1][0]:
                intervals[i][1] = max(intervals[i][1], intervals[i + 1][1])
                intervals.remove(intervals[i + 1])
                continue
            i += 1

        return intervals

# 162. Find Peak Element
# A peak element is an element that is strictly greater than its neighbors.
#
# Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.
#
# You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.
#
# You must write an algorithm that runs in O(log n) time.
class Find_Peak_Element:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        for i in range(len(nums)):
            if i == 0:
                if nums[i + 1] < nums[i]:
                    return i
            elif i == len(nums) - 1:
                if nums[i - 1] < nums[i]:
                    return i
            else:
                if nums[i - 1] < nums[i] and nums[i + 1] < nums[i]:
                    return i
        return -1

# 523. Continuous Subarray Sum
# Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.
#
# A good subarray is a subarray where:
#
# its length is at least two, and
# the sum of the elements of the subarray is a multiple of k.
# Note that:
#
# A subarray is a contiguous part of the array.
# An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.
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

# 88. Merge Sorted Array
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
#
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
#
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
class Merge_Sorted_Array:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        k = m + n - 1

        while j >= 0:
            if i >= 0 and nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

# 986. Interval List Intersections
# You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.
#
# Return the intersection of these two interval lists.
#
# A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.
#
# The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].
class Interval_List_Intersections:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ans = []
        i = j = 0

        while i < len(firstList) and j < len(secondList):
            lo = max(firstList[i][0], secondList[j][0])
            hi = min(firstList[i][1], secondList[j][1])

            if lo <= hi:
                ans.append([lo, hi])

            if firstList[i][1] <= secondList[j][1]:
                i += 1
            else:
                j += 1

        return ans

