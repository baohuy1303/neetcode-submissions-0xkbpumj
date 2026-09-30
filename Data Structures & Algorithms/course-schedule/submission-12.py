class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        for u, v in prerequisites:
            adj_list[u].append(v)
        
        seen = set()
        def dfs(i, path):
            if len(adj_list[i]) == 0:
                seen.add(i)
                return True

            path.add(i)

            for j in adj_list[i]:
                if j in path:
                    return False

                if j in seen:
                    continue
                        
                if dfs(j, path) == False:
                    return False
            
            seen.add(i)            
            path.remove(i)
            return True


        for i in range(numCourses):
            if i in seen:
                continue
            if dfs(i, set()) == False:
                return False

        return True