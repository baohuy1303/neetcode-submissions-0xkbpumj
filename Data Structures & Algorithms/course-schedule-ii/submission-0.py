class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # build dir graph like before 
        # verify no cycles

        preMap = {i:[] for i in range(numCourses)}
        for course, pre in prerequisites:
            preMap[course].append(pre)

        res = []
        visited, visiting = set(), set()
        def dfs(course):
            if course in visited:
                return True
            if course in visiting:
                return False

            visiting.add(course)
            for c in preMap[course]:
                if not dfs(c):
                    return False
            visiting.remove(course)
            visited.add(course)
            res.append(course)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
        return res
