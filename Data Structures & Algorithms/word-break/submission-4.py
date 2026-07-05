""" string s, dict wordDict

return true if s can be combined and made up from wordDict
same word in wordDict can be reused
only lowercase English letters

1 <= wordDict.length <= 1000 -> Worst case

~~instead of breaking the word down, we try to build from the dict
trying every combination of wordDict
-> O(n!)~~

we go thru each index and determine to split/match or not
-> O(2^n) (split or not split)

if matches then split and go down, have another not split

dfs(i) -> move until match and dfs(new_i) while another just keeps increasing new_i and try to match another """

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        res = [False]
        memo = {}
        wordDict = set(wordDict)

        def dfs(i):
            if i >= n:
                return True
    
            if i in memo:
                return memo[i]

            res = False
            for j in range(i, n+1):
                if s[i: j] in wordDict:
                    if dfs(j):
                        res = True
            memo[i] = res
            return res

        return dfs(0)