class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        dir = [(1,0), (-1,0), (0,-1), (0, 1)]
        seen = set()
        def recurse(r, c, k):
            if k >= len(word):
                return True
            
            for dr, dc in dir:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == word[k]:
                    if (nr, nc) in seen:
                        continue
                        
                    seen.add((nr, nc))
                    if recurse(nr, nc, k+1):
                        return True
                    seen.remove((nr,nc))
            
            return False
        
        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0]:
                    seen.add((r,c))
                    if recurse(r, c, 1):
                        return True
                    seen.remove((r,c))

        return False