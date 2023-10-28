# 480. Sliding Window Median
# The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle values.
#
# For examples, if arr = [2,3,4], the median is 3.
# For examples, if arr = [1,2,3,4], the median is (2 + 3) / 2 = 2.5.
# You are given an integer array nums and an integer k. There is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.
#
# Return the median array for each window in the original array. Answers within 10-5 of the actual value will be accepted.
from sortedcontainers import SortedList


class Sliding_Window_Median:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        lst = SortedList()

        res = []
        for i in range(len(nums)):
            lst.add(nums[i])
            if len(lst) > k:
                lst.remove(nums[i - k])
            if len(lst) == k:
                median = lst[k // 2] if k % 2 == 1 else (lst[k // 2 - 1] + lst[k // 2]) / 2
                res.append(median)

        return res