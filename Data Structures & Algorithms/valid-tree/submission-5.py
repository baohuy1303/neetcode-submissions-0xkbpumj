''' n nodes 0 -> n-1
list of undir edges [nodeA, nodeB]... - goes both ways
no duplicate edges

Valid tree:
- n-1 edges
- acyclic = no cycle
- connected

Check right away n-1 edges

2 Pass, build the graph then dfs with a seen set.

If seen set < n 
-> Disconnected

adj_list # val: [list of neighbors]

O(n) '''

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != (n-1):
            return False

        adj_list = {i:[] for i in range(n)}
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        seen = set()
        def dfs(node, parent):
            if node in seen:
                return False

            seen.add(node)
            for neighbor in adj_list[node]:
                if neighbor == parent:
                    continue
                if not dfs(neighbor, node):
                    return False
            return True

        if not dfs(0, 0):
            return False

        if len(seen) < n:
            return False
        return True
