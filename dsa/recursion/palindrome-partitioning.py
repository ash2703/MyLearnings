"""
Given a string s, partition s such that every 
substring of the partition is a palindrome

Return all possible palindrome partitioning of s.

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
"""

from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        print(n)
        partitions = []

        def isPalindrome(s):
            if len(s) == 1:
                return True
            return s == s[::-1]

        def partitionHelper(idx, res):
            # print(idx, res)
            if idx == n:
                # print("Adding to solution")
                partitions.append(res.copy())
                return

            for i in range(idx, n):
                if isPalindrome(s[idx : i + 1]):
                    res.append(s[idx : i + 1])
                    partitionHelper(i + 1, res)
                    res.pop()

        partitionHelper(0, [])
        return partitions


if __name__ == "__main__":
    sol = Solution()
    print(sol.partition("aab"))
    print(sol.partition("a"))
