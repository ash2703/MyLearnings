"""
Problem statement
You are given ‘n’ cities, some of which are connected by bidirectional roads. 
You are also given an ‘n x n’ matrix i.e. ‘roads’, 
where if city ‘i’ and ‘j’ are connected by a road then ‘roads[i][j]'= 1, 
otherwise ‘roads[i][j]' = 0.

A province is a group of cities that are either directly or indirectly connected to each other through roads.

The goal is to count and return the total number of such provinces in the given matrix.

Example:
n = 4, roads = [ [1, 1, 1, 0],
                 [1, 1, 1, 0],
                 [1, 1, 1, 0],
                 [0, 0, 0, 1] ]
"""

from typing import List


def findNumOfProvinces(roads: List[List[int]], n: int) -> int:
    visited = [False] * n
    cities = 0
    dfs = []

    def traverse(node):
        visited[node] = True
        for connections, connected in enumerate(roads[node]):
            if connected:
                if not visited[connections]:
                    dfs.append(connections)
                    visited[connections] = True
                    traverse(connections)

    for node in range(len(visited)):
        if not visited[node]:
            cities += 1
            dfs.append(node)
            traverse(node)

    return cities, dfs


if __name__ == "__main__":
    cities, dfs = findNumOfProvinces(
        [[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 1], [0, 0, 1, 1]], 4
    )
    print(cities, dfs)
