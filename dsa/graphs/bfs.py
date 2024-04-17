"""
Problem statement
Given an adjacency list representation of a directed graph with ‘n’ vertices and ‘m’ edges. Your task is to return a list consisting of Breadth-First Traversal (BFS) starting from vertex 0.

In this traversal, one can move from vertex 'u' to vertex 'v' only if there is an edge from 'u' to 'v'. The BFS traversal should include all nodes directly or indirectly connected to vertex 0.

Note:
The traversal should proceed from left to right according to the input adjacency list.


Example:
Adjacency list: { {1,2,3},{4}, {5}, {},{},{}}

The interpretation of this adjacency list is as follows:
Vertex 0 has directed edges towards vertices 1, 2, and 3.
Vertex 1 has a directed edge towards vertex 4.
Vertex 2 has a directed edge towards vertex 5.
Vertices 3, 4, and 5 have no outgoing edges.

We can also see this in the diagram below.

BFS traversal: 0 1 2 3 4 5
"""

from typing import List
from collections import deque


def bfsTraversal(n: int, adj: List[List[int]]) -> List[int]:
    # write your code here
    traversed = [False] * n
    order = deque()
    bfs = []
    curr_node = 0
    order.append(curr_node)
    traversed[curr_node] = True
    while len(order):
        curr_node = order.popleft()
        print("Queue: ", order)
        print("Traversing node: ", curr_node)
        for edge in adj[curr_node]:
            if not traversed[edge]:
                print("Adding edge: ", edge)
                order.append(edge)
                traversed[edge] = True
        print("Popping: ", curr_node)
        bfs.append(curr_node)
    return bfs

if __name__ == "__main__":
    adj = [[10, 7], [8, 9], [16, 3, 4, 1], [4, 0, 8], [17], [12, 9, 7], [13, 17, 3, 8, 6, 15, 0], [13, 16, 14, 15, 4], [8], [9, 4, 17, 7, 16, 12, 0], [16, 7, 17], [4, 5, 6, 15, 0, 12, 10, 1], [1, 17, 4], [13, 17, 12], [6, 14, 5, 0], [5, 1], [17, 14], [8, 14]]
    bfsTraversal(18, adj)