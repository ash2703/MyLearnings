"""
Consider a rat placed at (0, 0) in a square matrix of order N * N. It has to reach the destination at (N - 1, N - 1). 
Find all possible paths that the rat can take to reach from source to destination. 
The directions in which the rat can move are 'U'(up), 'D'(down), 'L' (left), 'R' (right). 
Value 0 at a cell in the matrix represents that it is blocked and rat cannot move to it while value 1 at a cell in the matrix represents that rat can be travel through it.
Note: In a path, no cell can be visited more than one time. If the source cell is 0, the rat cannot move to any other cell.

Example 1:

Input:
N = 4
m[][] = {{1, 0, 0, 0},
         {1, 1, 0, 1}, 
         {1, 1, 0, 0},
         {0, 1, 1, 1}}
Output: DDRDRR DRDDRR
Explanation:
The rat can reach the destination at 
(3, 3) from (0, 0) by two paths - DRDDRR 
and DDRDRR, when printed in sorted order 
we get DDRDRR DRDDRR.

Example 2:
Input:
N = 2
m[][] = {{1, 0},
         {1, 0}}
Output: -1
Explanation:
No path exists and destination cell is blocked.
"""


class Solution:
    def findPath(self, m, n):
        print(m, n)
        if m[n - 1][n - 1] == 0 or m[0][0] == 0:
            return []
        paths = []

        def traverse(x, y, path):
            if x == y == (n - 1):
                print(path)
                paths.append("".join(path))
                return

            m[x][y] = 0

            up = x - 1, y
            down = x + 1, y
            left = x, y - 1
            right = x, y + 1

            for (dx, dy), move in zip([up, down, left, right], ["U", "D", "L", "R"]):
                if (0 <= dx < n) and (0 <= dy < n):
                    if m[dx][dy] == 0:
                        continue
                    print("traversing", dx, dy, move)
                    path.append(move)
                    traverse(dx, dy, path)
                    path.pop()

            m[x][y] = 1

        print("Starting")
        traverse(0, 0, [])

        return paths


if __name__ == "__main__":
    sol = Solution()
    ans = sol.findPath([[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]], 4)
    print("Answer", ans)
