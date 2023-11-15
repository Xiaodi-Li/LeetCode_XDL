# 670. Maximum Swap
# You are given an integer num. You can swap two digits at most once to get the maximum valued number.
#
# Return the maximum valued number you can get.
class Maximum_Swap:
    def maximumSwap(self, num: int) -> int:
        numstr = str(num)

        maxdigit = -1
        maxidx = -1
        leftidx = -1
        rightidx = -1

        for i in range(len(numstr) - 1, -1, -1):
            if int(numstr[i]) > maxdigit:
                maxdigit = int(numstr[i])
                maxidx = i
                continue

            if int(numstr[i]) < maxdigit:
                leftidx = i
                rightidx = maxidx

        if leftidx == -1:
            return num

        numlist = list(numstr)
        numlist[leftidx], numlist[rightidx] = numlist[rightidx], numlist[leftidx]
        return int(''.join(numlist))

# 283. Move Zeroes
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#
# Note that you must do this in-place without making a copy of the array.
class Move_Zeroes:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0

        for fast in range(len(nums)):
            if nums[fast] != 0 and nums[slow] == 0:
                nums[fast], nums[slow] = nums[slow], nums[fast]

            if nums[slow] != 0:
                slow += 1

        return nums

# 296. Best Meeting Point
# Given an m x n binary grid grid where each 1 marks the home of one friend, return the minimal total travel distance.
#
# The total travel distance is the sum of the distances between the houses of the friends and the meeting point.
#
# The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.
class Best_Meeting_Point:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        row_sum = list(map(sum, grid))
        col_sum = list(map(sum, zip(*grid)))

        def minTotalDistance1D(vec):
            i, j = -1, len(vec)
            left = right = 0
            d = 0

            while i != j:
                if left < right:
                    d += left
                    i += 1
                    left += vec[i]
                else:
                    d += right
                    j -= 1
                    right += vec[j]
            return d

        return minTotalDistance1D(row_sum) + minTotalDistance1D(col_sum)



