class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # must have n-1 edges
        # no cycle
        # dfs each node and see if theres a cycle

        if len(edges) != n-1:
            return False

        adj_list = { i:[] for i in range(n)}
        for x, y in edges:
            adj_list[x].append(y)
            adj_list[y].append(x)

        def dfs(parent, node, visited):
            if node in visited:
                return False
            
            visited.add(node)
            for neighbor in (adj_list[node]):
                if neighbor == parent:
                    continue
                if not dfs(node, neighbor, visited):
                    return False
            visited.remove(node)
            return True
        
        for i in range(n):
            if not dfs(-1, i, set()):
                return False

        return True


        