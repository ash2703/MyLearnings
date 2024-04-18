"""
Problem statement
You have been given an undirected graph with 'N' vertices and 'M' edges. The vertices are labelled from 1 to 'N'.

Your task is to find if the graph contains a cycle or not.

A path that starts from a given vertex and ends at the same vertex traversing the edges only once is called a cycle.

Example :

In the below graph, there exists a cycle between vertex 1, 2 and 3. 

Note:

1. There are no parallel edges between two vertices.

2. There are no self-loops(an edge connecting the vertex to itself) in the graph.

3. The graph can be disconnected.
For Example :

Input: N = 3 , Edges =  [[1, 2], [2, 3], [1, 3]].
Output: Yes

Explanation : There are a total of 3 vertices in the graph. There is an edge between vertex 1 and 2, vertex 2 and 3 and vertex 1 and 3. So, there exists a cycle in the graph. 
Detailed explanation ( Input/output format, Notes, Images )
Constraints:
1 <= T <= 10
1 <= N <= 5000
0 <= M <= min(5000, (N * (N - 1)) / 2)
1 <= edges[i][0] <= N 
1 <= edges[i][1] <= N 

Time Limit: 1 sec 
Sample Input 1:
1
3 2
1 2
2 3
Sample output 1:
No
Explanation of Sample output 1:
 The above graph can be represented as 

There are a total of 3 vertices in the graph.There is an edge between vertex 1 and 2 and vertex 2 and 3. So, there is no cycle present in the graph. 
Sample Input 2:
2
4 0 
4 3
1 4
4 3
3 1
Sample output 2:
No
Yes
"""

from collections import deque


def cycleDetection(edges, n, m):
    adjList = [[] for _ in range(n + 1)]
    for pair in edges:
        adjList[pair[0]].append(pair[1])
        adjList[pair[1]].append(pair[0])

    order = deque()
    visited = [-1] * (n + 1)

    def dfs(node, parent):
        visited[node] = 1
        for neighbour in adjList[node]:
            if visited[neighbour] == -1:
                if dfs(neighbour, node):
                    return True
            elif neighbour != parent:
                return True
        return False

    for node, value in enumerate(visited):
        if node == 0:
            continue
        if visited[node] == -1:
            if dfs(node, -1):
                return "Yes"
    return "No"


if __name__ == "__main__":
    print(cycleDetection([[1, 2], [2, 3]], 3, 2))
