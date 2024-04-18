"""
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

 

Example 1:


Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Notice that an 'O' should not be flipped if:
- It is on the border, or
- It is adjacent to an 'O' that should not be flipped.
The bottom 'O' is on the border, so it is not flipped.
The other three 'O' form a surrounded region, so they are flipped.
Example 2:

Input: board = [["X"]]
Output: [["X"]]
"""

from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])

        # 0, n or rows, n
        # n, 0 or n, cols
        nodes = []
        for row in range(rows):
            for col in [0, cols - 1]:
                if board[row][col] == "O":
                    nodes.append((row, col))
        for row in [0, rows - 1]:
            for col in range(cols):
                if board[row][col] == "O":
                    nodes.append((row, col))

        def dfs(node):
            row, col = node
            board[row][col] = -1
            top = row - 1, col
            bottom = row + 1, col
            left = row, col - 1
            right = row, col + 1
            for x, y in [top, bottom, left, right]:
                if x < 0 or y < 0 or x >= rows or y >= cols:
                    continue
                if board[x][y] == "O":
                    dfs((x, y))

        for node in nodes:
            x, y = node
            if board[x][y] != -1:
                dfs((x, y))

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == -1:
                    board[row][col] = "O"
                elif board[row][col] == "O":
                    board[row][col] = "X"
        # return board


if __name__ == "__main__":
    sol = Solution()
    board = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"],
    ]
    print(board)
    time_taken = sol.solve(board)
    print(board)
