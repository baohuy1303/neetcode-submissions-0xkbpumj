''' labeled from 1 to n.
INITIALLY, no cycles and n-1 edges (connected)

return the extra edge that can be removed, without breaking connectivity

what determines if a graph is all connected?
    - at least n-1 edges
    - from 1 vertex we can travel to every other vertex

brute-force: try remove, check if connected. continue until end -> O(E*V)

Iterate edges. Mark all the vertices that was present. If we face an edge that has both vertices marked,
its redundant?
But what happens with [[1,3], [1,2], [4,5]]? This is still disconnected

how do we maintain a way to check connectivity while traversing thru edges?
    - bfs on current marked list and see if can mark all the current vertices seen? But this
    would still be brute force

-> Union Find but i dont remember :/
 '''
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        parents = list(range(N+1))
        rank = [1] * (N+1)

        def find(node):
            if node == parents[node]:
                return node
            parents[node] = find(parents[node])
            return parents[node]

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                parents[p2] = p1
                rank[p1] += rank[p2]
            else:
                parents[p1] = p2
                rank[p2] += rank[p1]
            return True

        for u, v in edges:
            if union(u, v) == False:
                return [u,v]
        return []   

