"""
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and color. 
You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, 
plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, 
plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. 
Replace the color of all of the aforementioned pixels with color.

Return the modified image after performing the flood fill.

Example 1:

Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.

Example 2:

Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
Output: [[0,0,0],[0,0,0]]
Explanation: The starting pixel is already colored 0, so no changes are made to the image.
"""

from collections import deque
from typing import List


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        og_pixel_color = image[sr][sc]
        if og_pixel_color == color:
            return image

        order = deque()
        row, col = len(image), len(image[0])

        image[sr][sc] = color
        order.append((sr, sc))

        while order:
            x, y = order.popleft()
            top = x - 1, y
            bottom = x + 1, y
            left = x, y - 1
            right = x, y + 1
            for pixel_x, pixel_y in [top, bottom, left, right]:
                # print(image)
                if pixel_x < 0 or pixel_x >= row or pixel_y < 0 or pixel_y >= col:
                    continue
                # print("moving: ", pixel_x, pixel_y)
                if image[pixel_x][pixel_y] == og_pixel_color:
                    image[pixel_x][pixel_y] = color
                    order.append((pixel_x, pixel_y))
        return image


if __name__ == "__main__":
    sol = Solution()
    image = sol.floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr=1, sc=1, color=2)
    print(image)
