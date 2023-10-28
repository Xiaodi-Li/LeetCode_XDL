# 498. Diagonal Traverse
# Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.
class Diagonal_Traverse:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        d = {}

        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if i + j not in d:
                    d[i + j] = [mat[i][j]]
                else:
                    d[i + j].append(mat[i][j])

        ans = []
        for entry in d.items():
            if entry[0] % 2 == 0:
                [ans.append(x) for x in entry[1][::-1]]
            else:
                [ans.append(x) for x in entry[1]]

        return ans


# 1424. Diagonal Traverse II
# Given a 2D integer array nums, return all elements of nums in diagonal order as shown in the below images.
class Diagonal_Traverse_II:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diag_dict = {}

        for row in range(len(nums) - 1, -1, -1):
            for col in range(len(nums[row]) - 1, -1, -1):
                if row + col in diag_dict:
                    diag_dict[row + col].append(nums[row][col])
                else:
                    diag_dict[row + col] = [nums[row][col]]

        ans = []
        curr = 0

        while curr in diag_dict:
            ans.extend(diag_dict[curr])
            curr += 1

        return ans

