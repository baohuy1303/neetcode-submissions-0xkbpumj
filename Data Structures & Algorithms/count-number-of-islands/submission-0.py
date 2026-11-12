class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(i, j):
            seen.add((i,j))

            for dr, dc in dir:
                nr = i + dr
                nc = j + dc

                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                    if (nr, nc) not in seen and grid[nr][nc] == "1":
                        dfs(nr, nc)

            return


        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i , j) not in seen and grid[i][j] == "1":
                    dfs(i, j)
                    res += 1

        return res
            