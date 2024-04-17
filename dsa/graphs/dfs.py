"""
You are given a connected undirected graph. Perform a Depth First Traversal of the graph.
"""


class Solution:
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        # code here
        visited = [False] * V
        dfs = []
        
        def dfsHelper(curr_node):
            dfs.append(curr_node)
            # print("Shouting ", curr_node)
            for node in adj[curr_node]:
                if not visited[node]:
                    # print("Visiting: ", node)
                    visited[node] = True
                    dfsHelper(node)
        
        visited[0] = True
        dfsHelper(0)
        
        return dfs