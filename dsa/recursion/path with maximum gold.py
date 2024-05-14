"""
In a gold mine grid of size m x n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.

Return the maximum amount of gold you can collect under the conditions:

Every time you are located in a cell you will collect all the gold in that cell.
From your position, you can walk one step to the left, right, up, or down.
You can't visit the same cell more than once.
Never visit a cell with 0 gold.
You can start and stop collecting gold from any position in the grid that has some gold.
 

Example 1:

Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
Output: 24
Explanation:
[[0,6,0],
 [5,8,7],
 [0,9,0]]
Path to get the maximum gold, 9 -> 8 -> 7.
Example 2:

Input: grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
Output: 28
Explanation:
[[1,0,7],
 [2,0,6],
 [3,4,5],
 [0,3,0],
 [9,0,20]]
Path to get the maximum gold, 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7.
"""

from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])

        def traverse(x, y, gold_sum, path):
            if x < 0 or x >= row or y < 0 or y >= col or grid[x][y] == 0:
                print(path, gold_sum)
                return gold_sum
            current_gold = grid[x][y]
            path.append(current_gold)
            gold_sum += current_gold
            max_gold = gold_sum

            grid[x][y] = 0
            up, down, left, right = (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)
            for dir_x, dir_y in [up, down, left, right]:
                max_gold = max(max_gold, traverse(dir_x, dir_y, gold_sum, path))

            grid[x][y] = current_gold
            path.pop()
            return max_gold

        max_gold = 0
        for x in range(row):
            for y in range(col):
                if grid[x][y] == 0:
                    continue
                max_gold = max(max_gold, traverse(x, y, 0, []))

        return max_gold
