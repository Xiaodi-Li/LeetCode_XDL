# 398. Random Pick Index
# Given an integer array nums with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.
#
# Implement the Solution class:
#
# Solution(int[] nums) Initializes the object with the array nums.
# int pick(int target) Picks a random index i from nums where nums[i] == target. If there are multiple valid i's, then each index should have an equal probability of returning.
class Random_Pick_Index:

    def __init__(self, nums: List[int]):
        self.indices = {}
        for i, num in enumerate(nums):
            if num not in self.indices:
                self.indices[num] = [i]
            else:
                self.indices[num].append(i)

    def pick(self, target: int) -> int:
        indices = self.indices[target]
        pick_one = random.choice(indices)
        return pick_one

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)