''' 2 strings, only english letters
STRING t is STATIC, its there to check not move

how do we know they are distinct?
    - we only move thru it once

how can we check if a subsequence is the same?
    - have both pointers
    - check first char:
        - match first char and move both pointers up to shrink the next prob down
        - if not match:
            - try moving left and keep right to compare a new subproblem

how do we keep a running total of subsequences to keep iterating even when we match 1?
    - after we have found a match, we add it to total
    - we continously shrink/skip the left while keeping right even when we have found a match
    to discover all the distinct subsequences that matches

Brute force: 2^(s*t)
Memo: s*t

Base: i >= len(s) but j not at the end -> we havent found a match
 '''

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}
        def dfs(i, j):
            if j >= len(t):
                return 1
            if i >= len(s) and j < len(t):
                return 0
            
            if (i,j) in memo:
                return memo[(i,j)]

            match = 0
            if s[i] == t[j]:
                match = dfs(i+1, j+1)
            skip = dfs(i+1, j)
            memo[(i,j)] = skip + match
            return skip + match
        
        return dfs(0,0)
            