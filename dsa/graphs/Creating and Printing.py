"""
Problem statement
You are given an undirected graph of 'N' nodes and 'M' edges. Your task is to create the graph and print the adjacency list of the graph. It is guaranteed that all the edges are unique, i.e., if there is an edge from 'X' to 'Y', then there is no edge present from 'Y' to 'X' and vice versa. Also, there are no self-loops present in the graph.

In graph theory, an adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a vertex in the graph.

For Example:
If 'N' = 3 and edges = {{2,1}, {2,0}}.

So, the adjacency list of the graph is stated below.
0 → 2
1 → 2
2 → 0 → 1
"""

from typing import List, Tuple


def printAdjacency(n: int, m: int, edges: List[Tuple[int, int]]) -> List[List[int]]:
    adjList = [[i] for i in range(n)]
    for a, b in edges:
        adjList[a].append(b)
        adjList[b].append(a)
    return adjList
