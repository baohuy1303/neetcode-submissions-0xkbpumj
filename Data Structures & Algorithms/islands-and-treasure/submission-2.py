from collections import deque 
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # start at treasure and fill as we go
        # dfs 25 mins
        # dfs slow, forgot to evaluate time

        # bfs hold (i, j, dist)

        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    q.append((i, j, 0))

        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while q:
            r, c, dist = q.popleft()
            for dr, dc in dir:
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                    if grid[nr][nc] != -1 and grid[nr][nc] != 0 and (dist + 1) < grid[nr][nc]:
                        grid[nr][nc] = dist + 1
                        q.append((nr, nc, dist + 1))
        return



            