"""
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

 

Example 1:


Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]
Example 2:


Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
"""

from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row, col = len(mat), len(mat[0])
        order = deque()
        visited = [[-1 for _ in range(col)] for _ in range(row)]

        for i in range(row):
            for j in range(col):
                # print(i, j)
                if mat[i][j] == 0:
                    order.append((i, j, 0))
                    visited[i][j] = 0

        while order:
            # print(visited)
            x, y, dist = order.popleft()

            top = x - 1, y
            bottom = x + 1, y
            left = x, y - 1
            right = x, y + 1

            for r, c in [top, bottom, left, right]:
                if r < 0 or c < 0 or r >= row or c >= col:
                    continue
                # print(r, c, dist)
                if visited[r][c] == -1:
                    visited[r][c] = dist + 1
                    order.append((r, c, dist + 1))
        return visited


if __name__ == "__main__":
    sol = Solution()
    updated = sol.updateMatrix([[0, 0, 0, 1], [0, 1, 0, 0], [0, 0, 0, 1]])
    print(updated)
