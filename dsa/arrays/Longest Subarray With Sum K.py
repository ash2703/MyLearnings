""" 
This is the optimal solution for arrays with negaitve elements
Ninja and his friend are playing a game of subarrays. They have an array ‘NUMS’ of length ‘N’. Ninja’s friend gives him an arbitrary integer ‘K’ and asks him to find the length of the longest subarray in which the sum of elements is equal to ‘K’.

Ninjas asks for your help to win this game. Find the length of the longest subarray in which the sum of elements is equal to ‘K’.

If there is no subarray whose sum is ‘K’ then you should return 0.

Example:
Input: ‘N’ = 5,  ‘K’ = 4, ‘NUMS’ = [ 1, 2, 1, 0, 1 ]

Output: 4

There are two subarrays with sum = 4, [1, 2, 1] and [2, 1, 0, 1]. Hence the length of the longest subarray with sum = 4 is 4.
"""

from typing import List


def getLongestSubarray(nums: List[int], k: int) -> int:
    # Write your code here
    found = dict()
    psum = 0
    max_counter = 0
    for i, num in enumerate(nums):
        psum += num
        if psum == k:
            max_counter = max(
                max_counter, i + 1
            )  # This handles the case of not having 0 in our hashmap

        if psum - k in found:
            max_counter = max(max_counter, i - found[psum - k])
        if (
            psum not in found
        ):  # If we add without checking, array having 0s will create issue
            found[psum] = i
    return max_counter
