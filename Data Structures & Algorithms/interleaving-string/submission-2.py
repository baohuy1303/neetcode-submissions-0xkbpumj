class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
            
        memo = {}
        def dfs(i, j):
            if i + j >= len(s3):
                return True
            if (i,j) in memo:
                return memo[(i,j)]
            res = False
            if i < len(s1) and s1[i] == s3[i+j] and dfs(i+1, j):
                res = True
            if j < len(s2) and s2[j] == s3[i+j] and dfs(i, j+1):
                res = True
            memo[(i,j)] = res
            return res
        
        return dfs(0, 0)
                