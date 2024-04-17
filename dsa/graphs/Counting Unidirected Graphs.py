"""
Problem statement
Return the number of undirected graphs that can be formed using 'N' vertices, allowing for disconnected components within the graph. Self-edges and multiple edges are not allowed.

For Example:
For N = 2,
Count is 2.
Consider the vertices to be ‘A’ and ‘B’.
These are the possible 2 graphs
"""

from typing import *


def countingGraphs(N: int) -> int:
    """
    There are NC2 ways to select 2 nodes from N nodes.
    Since the graph is undirected, the edge between the 2 nodes can be in 2 ways.
    For each pair of nodes, there can be 2 possible edges between them.
    So, the total number of ways to form an undirected graph is 2^(N*(N-1)/2).
    """
    # Write your code here
    node_selection = N * (N - 1) // 2

    return 2**node_selection


def countingDirectedGraphs(N: int) -> int:
    """
    There are NC2 ways to select 2 nodes from N nodes.
    Since the graph is directed, the edge between the 2 nodes can be in 4 ways.
    The ways are:
    1. Node 1 to Node 2
    2. Node 2 to Node 1
    3. Node 1 to Node 2 and Node 2 to Node 1
    4. No edge between Node 1 and Node 2
    So, the total number of ways to form an directed graph is 4^(N*(N-1)/2).
    """

    node_selection = N * (N - 1) // 2
    return 4**node_selection
