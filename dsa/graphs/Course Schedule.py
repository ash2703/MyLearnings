"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
"""

from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = [[] for _ in range(numCourses)]
        for pair in prerequisites:
            adjList[pair[0]].append(pair[1])

        # print(adjList)
        visited = [False] * numCourses
        traversed = [
            False
        ] * numCourses  # To keep track of nodes that are being traversed

        def dfs(node):
            # print(node)
            for neighbour in adjList[node]:
                # print("Checking neighbour ", neighbour)
                if visited[neighbour] and traversed[neighbour]:
                    # print("Neighbour visited already ", neighbour)
                    return False
                if not visited[neighbour]:
                    visited[neighbour] = True
                    traversed[neighbour] = True
                    if not dfs(neighbour):
                        return False
                    traversed[neighbour] = False
            return True

        for i in range(numCourses):
            if visited[i] == False:
                visited[i] = True
                traversed[i] = True
                if not dfs(i):
                    return False
                traversed[i] = False
        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.canFinish(2, [[1, 0], [0, 1]]))
