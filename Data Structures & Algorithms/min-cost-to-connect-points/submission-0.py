import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # adjacency list
        # create a min heap, and we can try starting from anywhere
        # add the weights, neighbor nodes of cur onto the minheap
        # pop min and add to visited
        # check if visited == len(points)

        n = len(points)
        adj = {i:[] for i in range(n)}
        for i in range(n):
            for j in range(n):
                adj[i].append(((abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])), j))
        
        # weight, index of node
        heap = [(0, 0)]
        visited = set()
        res = 0
        while len(visited) < len(points):
            while heap[0][1] in visited:
                heapq.heappop(heap)

            node = heapq.heappop(heap)
            visited.add(node[1])
            res += node[0]
            for neighbor in adj[node[1]]:
                heapq.heappush(heap, neighbor)
        return res            

