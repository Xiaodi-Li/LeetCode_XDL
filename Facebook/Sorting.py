# 1331. Rank Transform of an Array
# Given an array of integers arr, replace each element with its rank.
#
# The rank represents how large the element is. The rank has the following rules:
#
# Rank is an integer starting from 1.
# The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
# Rank should be as small as possible.

class Rank_Transform:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = sorted(arr)
        arr_dict = {}
        index = 0

        for item in sorted_arr:
            if item not in arr_dict:
                index += 1
                arr_dict[item] = index

        res = [arr_dict[item] for item in arr]
        return res