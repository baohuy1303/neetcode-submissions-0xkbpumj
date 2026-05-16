class Solution:
    def numDecodings(self, s: str) -> int:
        # take 1 or 2 digits at current str
        # str slicing takes O(n)
        memo = {}
        def dfs(i):
            res = 0
            if i >= len(s):
                return 1
            if s[i] == '0':
                return 0
            if i in memo:
                return memo[i]
            if i < len(s) - 1:
                if s[i] == '1' or (s[i] == '2' and s[i+1] in '0123456'):
                    memo[i+2] = dfs(i+2)
                    res += memo[i+2]
            memo[i+1] = dfs(i+1)
            res += memo[i+1]
            return res
            
        return dfs(0)
            
            
            

