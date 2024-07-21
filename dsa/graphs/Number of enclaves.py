"""
You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.

Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.

 

Example 1:


Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
Output: 3
Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.
Example 2:


Input: grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
Output: 0
Explanation: All 1s are either on the boundary or can reach the boundary.
"""

from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        nodes = []
        for row in range(rows):
            for col in [0, cols - 1]:
                if grid[row][col] == 1:
                    nodes.append((row, col))

        for row in [0, rows - 1]:
            for col in range(cols):
                if grid[row][col] == 1:
                    nodes.append((row, col))

        # print(nodes)
        def dfs(node):
            row, col = node
            grid[row][col] = 0
            top = row - 1, col
            bottom = row + 1, col
            left = row, col - 1
            right = row, col + 1

            for x, y in [top, bottom, left, right]:
                if 0 <= x < rows and 0 <= y < cols:
                    if grid[x][y] == 1:
                        # print(x, y)
                        dfs((x, y))

        for node in nodes:
            x, y = node
            if grid[x][y] == 0:
                continue
            dfs(node)
        # print(grid)
        enclaves = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    enclaves += 1

        return enclaves


if __name__ == "__main__":
    sol = Solution()
    num_enclaves = sol.numEnclaves(
        [[0, 1, 1, 0], [0, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0]]
    )
    print(num_enclaves)
