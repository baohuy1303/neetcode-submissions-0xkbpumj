class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # start at treasure and fill as we go

        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(i, j, dist):
            grid[i][j] = min(dist, grid[i][j])

            for dr, dc in dir:
                nr = i + dr
                nc = j + dc

                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                    if grid[nr][nc] != -1 and dist < grid[nr][nc] and grid[nr][nc] != 0:
                        dfs(nr, nc, dist + 1)
            return
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    for dr, dc in dir:
                        nr = i + dr
                        nc = j + dc

                        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                            if grid[nr][nc] != -1 and grid[nr][nc] != 0:
                                dfs(nr, nc, 1)


            