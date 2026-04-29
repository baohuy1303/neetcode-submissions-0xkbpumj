class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ''' at each we have option to open or close'''
        res = []
        def dfs(p, path, open, close):
            
            if close > open:
                return

            if len(path) == n*2:
                res.append(path)
                return
            
            if open < n:
                dfs("(", path + "(", open+1, close)
            if close < n:
                dfs(")", path + ")", open, close+1)
            return
        
        dfs("", "", 0, 0)
        return res
            

        