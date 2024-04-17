"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. 
If this is impossible, return -1.

Example 1:

Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, 
because rotting only happens 4-directionally.

Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
"""

from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        order = deque()
        tot_unaffected = 0
        row, col = len(grid[0]), len(grid)
        visited = [[-1] * row for _ in range(col)]
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 2:
                    order.append((row, col, 0))
                    visited[row][col] = 2
                elif grid[row][col] == 1:
                    visited[row][col] = 1
                    tot_unaffected += 1
        t = 0
        # print(grid)
        # print(order)
        while order:
            # print(visited)
            r, c, t = order.popleft()
            top = r-1, c
            bottom = r+1, c
            left = r, c-1
            right = r, c+1
            for x, y in [top, bottom, left, right]:
                if x < 0 or y < 0 or x > row or y > col:
                    continue
                if visited[x][y] == 1:
                    tot_unaffected -= 1
                    # print("adding in queue: ", x, y, "time = ", t+1)
                    visited[x][y] = 2
                    order.append((x, y, t+1))
            # max_time = max(t, max_time)
        if tot_unaffected != 0: return -1
        return t

if __name__ == "__main__":
    sol = Solution()
    time_taken = sol.orangesRotting( [[2,1,1],[1,1,0],[0,1,1]])
    print(time_taken)
                
                    

