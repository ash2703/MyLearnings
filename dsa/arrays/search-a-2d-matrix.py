"""
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

"""

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        low = 0
        high = row - 1
        while low <= high:
            mid = (low + high) // 2
            mid_val = matrix[mid][-1]

            if mid_val < target:
                low = mid + 1
            elif mid_val > target:
                high = mid - 1
            else:
                return True

        if low >= row:
            return False
        start = 0
        end = col - 1
        while start <= end:
            mid = (end + start) // 2
            mid_val = matrix[low][mid]
            if mid_val == target:
                return True
            if mid_val > target:
                end = mid - 1
            else:
                start = mid + 1
        return False

        # O(n) method
        # sel_row = -1
        # for decide_row in range(row):
        #     if matrix[decide_row][-1] == target: return True
        #     if matrix[decide_row][-1] > target:
        #         sel_row = decide_row
        #         break
        # if sel_row == -1 : return False
        # for num in matrix[decide_row]:
        #     if num == target: return True
        # return False


if __name__ == "__main__":
    sol = Solution()
    print(sol.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 31))
