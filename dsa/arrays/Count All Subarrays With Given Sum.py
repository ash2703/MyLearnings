"""
Optimal soultion for arrays with non-negative elements
Problem statement
You are given an integer array 'arr' of size 'N' and an integer 'K'.

Your task is to find the total number of subarrays of the given array whose sum of elements is equal to k.

A subarray is defined as a contiguous block of elements in the array.

Example:
Input: ‘N’ = 4, ‘arr’ = [3, 1, 2, 4], 'K' = 6

Output: 2

Explanation: The subarrays that sum up to '6' are: [3, 1, 2], and [2, 4].
"""


def findAllSubarraysWithGivenSum(arr, s):
    # Write your code here.
    ptr1, ptr2 = 0, 0
    psum = arr[0]
    counter = 0
    while ptr2 < len(arr):
        while psum > s:
            psum -= arr[ptr1]
            ptr1 += 1
        if psum == s:
            counter += 1
        ptr2 += 1
        if ptr2 < len(arr):
            psum += arr[ptr2]
    return counter
