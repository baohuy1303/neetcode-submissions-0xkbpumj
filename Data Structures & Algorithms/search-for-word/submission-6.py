class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def dfs(i, j, seen, k):
            if k == len(word)-1 and board[i][j] == word[k]:
                return True
            if board[i][j] != word[k]:
                return False
            seen.add((i,j))
            for dr, dc in dir:
                nr = i + dr
                nc = j + dc

                if 0 <= nr < len(board) and 0 <= nc < len(board[0]):
                    if (nr, nc) in seen:
                        continue
                    if dfs(nr, nc, seen, k+1):
                        return True
            seen.remove((i,j))
            return False
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if dfs(i, j, set(), 0):
                    return True

        return False

            
