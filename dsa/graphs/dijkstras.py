import heapq


class Solution:

    # Function to find the shortest distance of all the vertices
    # from the source vertex S.
    def dijkstra(self, V, adj, S):
        distance = [float("inf")] * V
        priority_queue = [(0, S)]
        distance[S] = 0
        visited = set()
        # parent =
        # heapq.heappush(priority_queue, (0, S))

        while priority_queue:
            dist, node = heapq.heappop(priority_queue)
            print(dist, node, priority_queue)
            # if node in visited:
            #     continue
            visited.add(node)

            for adj_node, adj_dist in adj[node]:
                tot_distance = adj_dist + dist
                if tot_distance < distance[adj_node]:
                    distance[adj_node] = tot_distance
                    heapq.heappush(priority_queue, (adj_dist, adj_node))
        print(distance)
        return distance


if __name__ == "__main__":
    sol = Solution()
    sol.dijkstra(
        6,
        [
            [[3, 9], [5, 4]],
            [[4, 4]],
            [[5, 10]],
            [[0, 9]],
            [[1, 4], [5, 3]],
            [[0, 4], [2, 10], [4, 3]],
        ],
        1,
    )
