"""
Given an array nums of distinct integers, return all the possible permutations. 
You can return the answer in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
"""

from typing import List


class Solution:
    # Extra memory
    def permuteExtraMem(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        n = len(nums)

        def permutationHelper(perm, added):
            if len(perm) == n:
                permutations.append(perm.copy())
                return

            for i in range(0, n):
                if nums[i] in added:
                    continue
                perm.append(nums[i])
                added.add(nums[i])
                permutationHelper(perm, added)
                perm.pop()
                added.remove(nums[i])

        added = set()
        permutationHelper([], added)
        return permutations

    # No extra memory using swaps
    def permuteConstantMem(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        n = len(nums)

        def permutationHelper(idx):
            if idx == n:
                permutations.append(nums.copy())
                return

            for i in range(idx, n):
                nums[i], nums[idx] = nums[idx], nums[i]
                permutationHelper(idx + 1)
                nums[i], nums[idx] = nums[idx], nums[i]

        permutationHelper(0)
        return permutations


if __name__ == "__main__":
    sol = Solution()
    print(sol.permuteConstantMem([1, 2, 3]))
