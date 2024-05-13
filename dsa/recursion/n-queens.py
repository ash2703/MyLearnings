"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

Example 1:

Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
Example 2:

Input: n = 1
Output: [["Q"]]
"""

from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        unsafeRows = [0] * n
        unsafeCols = [0] * n
        unsafeDiag = [0] * ((2 * n) - 1)  # normal diagonal, top-left bottom right
        unsafeDiagT = [0] * ((2 * n) - 1)  # bottom left to top right
        mat = [
            ["." for _ in range(n)] for _ in range(n)
        ]  # Can also work by just saving queen positions in n size array
        solutions = []

        def isSafe(x, y):
            if (
                unsafeRows[x]
                or unsafeCols[y]
                or unsafeDiag[x - y + n - 1]
                or unsafeDiagT[x + y]
            ):
                return False
            return True

        def queenHelper(x, y, queenCount):
            if queenCount == n:
                solutions.append(["".join(row) for row in mat])
                return
            if x >= n or y >= n:
                return
            if isSafe(x, y):
                mat[x][y] = "Q"
                unsafeRows[x] = 1
                unsafeCols[y] = 1
                unsafeDiag[x - y + n - 1] = 1  # −(n−1) to n−1 adjusted to 0 to 2n−2
                unsafeDiagT[x + y] = 1
                # print("Placing queen at: ", x , y, "Tot queens now: ", queenCount + 1)
                queenHelper(0, y + 1, queenCount + 1)
                mat[x][y] = "."
                unsafeRows[x] = 0
                unsafeCols[y] = 0
                unsafeDiag[x - y + n - 1] = 0
                unsafeDiagT[x + y] = 0
            # print(f"Unable to place queen at col: {y} incrementing {x} -> {x + 1}")
            queenHelper(x + 1, y, queenCount)

        queenHelper(0, 0, 0)
        return solutions


if __name__ == "__main__":
    sol = Solution()
    print(sol.solveNQueens(8))
