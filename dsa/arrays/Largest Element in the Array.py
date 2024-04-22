"""
Problem statement
Given an array ‘arr’ of size ‘n’ find the largest element in the array.



Example:

Input: 'n' = 5, 'arr' = [1, 2, 3, 4, 5]

Output: 5

Explanation: From the array {1, 2, 3, 4, 5}, the largest element is 5.

"""


def largestElement(arr: [], n: int) -> int:

    # Write your code from here.
    largest = float("-inf")
    for num in arr:
        if num > largest:
            largest = num
    return largest
