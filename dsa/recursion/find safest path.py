"""
You are given a 0-indexed 2D matrix grid of size n x n, where (r, c) represents:

A cell containing a thief if grid[r][c] = 1
An empty cell if grid[r][c] = 0
You are initially positioned at cell (0, 0). In one move, you can move to any adjacent cell in the grid, including cells containing thieves.

The safeness factor of a path on the grid is defined as the minimum manhattan distance from any cell in the path to any thief in the grid.

Return the maximum safeness factor of all paths leading to cell (n - 1, n - 1).

An adjacent cell of cell (r, c), is one of the cells (r, c + 1), (r, c - 1), (r + 1, c) and (r - 1, c) if it exists.

The Manhattan distance between two cells (a, b) and (x, y) is equal to |a - x| + |b - y|, where |val| denotes the absolute value of val.

 

Example 1:


Input: grid = [[1,0,0],[0,0,0],[0,0,1]]
Output: 0
Explanation: All paths from (0, 0) to (n - 1, n - 1) go through the thieves in cells (0, 0) and (n - 1, n - 1).
Example 2:


Input: grid = [[0,0,1],[0,0,0],[0,0,0]]
Output: 2
Explanation: The path depicted in the picture above has a safeness factor of 2 since:
- The closest cell of the path to the thief at cell (0, 2) is cell (0, 0). The distance between them is | 0 - 0 | + | 0 - 2 | = 2.
It can be shown that there are no other paths with a higher safeness factor.
Example 3:


Input: grid = [[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]]
Output: 2
Explanation: The path depicted in the picture above has a safeness factor of 2 since:
- The closest cell of the path to the thief at cell (0, 3) is cell (1, 2). The distance between them is | 0 - 1 | + | 3 - 2 | = 2.
- The closest cell of the path to the thief at cell (3, 0) is cell (3, 2). The distance between them is | 3 - 3 | + | 0 - 2 | = 2.
It can be shown that there are no other paths with a higher safeness factor.
"""

from collections import deque
from typing import List


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        distanceThief = [[-1] * cols for _ in range(rows)]
        order = deque()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    order.append((row, col, 0))
        maxSafenessFactor = 0
        while order:
            row, col, distance = order.popleft()
            if distanceThief[row][col] != -1:  # Examine why this is necessary
                continue

            distanceThief[row][col] = distance
            maxSafenessFactor = max(maxSafenessFactor, distance)

            up = row - 1, col
            down = row + 1, col
            left = row, col - 1
            right = row, col + 1

            for dx, dy in [up, down, left, right]:
                if (0 <= dx < rows) and (0 <= dy < cols):
                    if distanceThief[dx][dy] == -1:
                        order.append((dx, dy, distance + 1))

        # print(distanceThief, maxSafenessFactor)

        def isSafe(x, y, safenessFactor):
            # print(x, y)
            if distanceThief[x][y] < safenessFactor:
                # print("Not possible")
                return False

            if x == y == rows - 1:
                # print(f"End is reachable with {safenessFactor}")
                return True

            up = x - 1, y
            down = x + 1, y
            left = x, y - 1
            right = x, y + 1

            currValue = grid[x][y]
            grid[x][y] = -1
            for dx, dy in [up, down, left, right]:
                if (0 <= dx < rows) and (0 <= dy < cols) and grid[dx][dy] != -1:
                    # print("Searching ", dx, dy)
                    if isSafe(dx, dy, safenessFactor):
                        grid[x][y] = currValue
                        return True

            grid[x][y] = currValue
            return False

        low, high = 0, maxSafenessFactor
        ans = 0
        while low <= high:
            mid = low + (high - low) // 2
            if isSafe(0, 0, mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.maximumSafenessFactor([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))  # 1
