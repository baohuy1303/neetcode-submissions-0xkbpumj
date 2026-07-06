class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n = numCourses
        adj_list = defaultdict(set) # course_number: (set of dependencies)
        
        for u, v in prerequisites:
            adj_list[u].add(v)
            
        visiting = set()
        visited = set()
        
        def dfs(node):
            if node in visiting:
                return False
            if node in visited:
                return True

            visiting.add(node)
            for d in adj_list[node]:
                if dfs(d) == False:
                    return False

            visiting.remove(node)
            visited.add(node)
            return True

        for node in range(n):
            if dfs(node) == False:
                return False
        
        return True