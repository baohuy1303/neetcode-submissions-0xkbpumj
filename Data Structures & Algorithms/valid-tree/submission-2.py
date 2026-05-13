class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # must have n-1 edges
        # no cycle
        # dfs each node and see if theres a cycle
        # global visited set bc all nodes should be able to reach (tree connectivity)

        if len(edges) != n-1:
            return False

        adj_list = { i:[] for i in range(n)}
        for x, y in edges:
            adj_list[x].append(y)
            adj_list[y].append(x)

        visited = set()
        def dfs(parent, node):
            if node in visited:
                return False
            
            visited.add(node)
            for neighbor in (adj_list[node]):
                if neighbor == parent:
                    continue
                if not dfs(node, neighbor):
                    return False
            return True
        
        return dfs(-1, 0) and len(visited) == n


        