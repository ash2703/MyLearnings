"""
The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"
Example 3:

Input: n = 3, k = 1
Output: "123"
"""

import math


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        out = []

        def permHelper(arr, k, out):
            n = len(arr)
            if n == 0:
                return
            combination = math.factorial(n - 1)
            place = (k - 1) // combination
            digit = arr.pop(place)
            out.append(digit)
            permHelper(arr, k % combination, out)

        arr = list(range(1, n + 1))
        permHelper(arr, k, out)
        return "".join(map(str, out))

        # # Brute force
        # permutations = []
        # n += 1
        # def permutationHelper(perm):
        #     if len(perm) == n - 1:
        #         permutations.append(perm.copy())

        #     for i in range(1, n):
        #         if i in perm: continue
        #         perm.append(i)
        #         permutationHelper(perm)
        #         perm.pop()
        # permutationHelper([])
        # # print(permutations)
        # return ''.join(map(str, permutations[k - 1]))


if __name__ == "__main__":
    sol = Solution()
    print(sol.getPermutation(3, 3))  # 213
