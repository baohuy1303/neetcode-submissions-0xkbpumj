class Solution:
    def numDecodings(self, s: str) -> int:
        # take 1 or 2 digits at current str
        memo = {}
        def dfs(num):
            res = 0
            if len(num) <= 1:
                if len(num) == 1 and int(num) == 0:
                    return 0 
                return 1
            if num in memo:
                return memo[num]
            cur_1 = int(num[0])
            cur_2 = int(num[0:2])

            if cur_1 > 0:
                memo[num[1:]] = dfs(num[1:])
                res += memo[num[1:]]
            if cur_2 - 10 >= 0 and cur_2 <= 26:
                memo[num[2:]] = dfs(num[2:])
                res += memo[num[2:]]
            return res
        
        return dfs(s)
            

