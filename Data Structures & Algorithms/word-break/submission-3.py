class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # have to use/split all of s
        # use a word, the rest is scanned
        # can reuse as many words in word dict
        # if remaining cant be found in dict, return False
        memo = {}
        wordDict = set(wordDict)
        def dfs(i):
            if i >= len(s):
                return True
            if i in memo:
                return memo[i]
            for j in range(len(s) - i):
                end = i + j
                if s[i:end + 1] in wordDict:
                    if dfs(end+1) == True:
                        return True
            memo[i] = False
            return memo[i]
        return dfs(0)