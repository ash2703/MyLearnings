"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
"""

from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        candidates.sort()
        # print(candidates)
        n = len(candidates)

        def combination(idx, tgt, result):
            if tgt == 0:
                # print("Adding: ", result)
                results.append(result.copy())
                return
            if idx == n:
                # print("Reached end")
                return

            for i in range(idx, n):
                # print(i, candidates[i], result, tgt)
                if i > idx and candidates[i - 1] == candidates[i]:
                    # print("Skipping")
                    continue
                if candidates[i] > tgt:
                    # print("Breaking")
                    break
                result.append(candidates[i])
                combination(i + 1, tgt - candidates[i], result)
                result.pop()

        combination(0, target, [])
        return results


if __name__ == "__main__":
    sol = Solution()
    print(sol.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
