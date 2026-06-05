''' 2 strings, both lowercase eng letters

three operations on word1 at any pos for UNLIMITED:
    - insert
    - delete
    - replace

word1 equal word2

- remove: i + 1 on word

these 2 needs j in bound
- replace: word1[i] = word2[j] (skip both)
- insert: if we keep inserting, we will reach the end of word2
        keep i, move j + 1
brute force: 3^(word1 + word2)
 '''
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        memo = {}

        def dfs(i, j):
            if i >= len(word1):
                if j < len(word2):
                    return len(word2) - j
                return 0
            if j >= len(word2):
                return len(word1) - i

            if (i,j) in memo:
                return memo[(i,j)]

            res = 0
            match = insert = remove = replace = float('inf')

            if word1[i] == word2[j]:
                match = dfs(i+1, j+1)
                
            if word1[i] != word2[j]:
                insert = 1 + dfs(i, j+1)
                remove = 1 + dfs(i+1, j)
                replace = 1 + dfs(i+1, j+1)
            
            res = min(match, insert, remove, replace)
            memo[(i,j)] = res
            return res
        return dfs(0,0)
