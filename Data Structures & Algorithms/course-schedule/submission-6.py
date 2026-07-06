class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n = numCourses
        adj_list = {i:[] for i in range(n)} # num: (dependencies)
        
        for u, v in prerequisites:
            adj_list[u].append(v)
            
        visiting = set()
        
        def dfs(node):
            if node in visiting:
                return False
            if len(adj_list[node]) == 0:
                return True

            visiting.add(node)
            for d in adj_list[node]:
                if dfs(d) == False:
                    return False

            visiting.remove(node)
            adj_list[node] = []
            return True

        for node in range(n):
            if dfs(node) == False:
                return False
        
        return True