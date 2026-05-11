class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build a directed graph
        # if theres a cycle then its invalid

        # labeled 0 to numCourses - 1 so this works
        preMap = { i:[] for i in range(numCourses)}

        for cur, pre in prerequisites:
            preMap[cur].append(pre)
        
        visiting = set()
        def dfs(cur):
            if cur in visiting:
                return False
            if len(preMap[cur]) == 0:
                return True
            visiting.add(cur)
            for prereq in preMap[cur]:
                if not dfs(prereq):
                    return False
            visiting.remove(cur)
            preMap[cur] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True           
            
