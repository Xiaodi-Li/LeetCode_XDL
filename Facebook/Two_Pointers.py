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
