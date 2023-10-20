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