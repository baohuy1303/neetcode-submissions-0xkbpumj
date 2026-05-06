class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # move until see a 1. if not in seen, dfs
        # explore 4 dir (check if out of bounds, or in seen or == 0 before dfs again)
        # return 1 + dfs

        max_len = 0
        seen = set()
        dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def dfs(row, col):
            area = 1
            seen.add(tuple([row, col]))

            for coords in dir:
                new_row = row + coords[0]
                new_col = col + coords[1]

                if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[new_row]):
                    if tuple([new_row, new_col]) in seen:
                        continue
                    if grid[new_row][new_col] == 1:
                        area += dfs(new_row, new_col)
                    
            return area
        
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == 1 and tuple([i, j]) not in seen:
                    new_len = dfs(i, j)
                    max_len = max(max_len, new_len)

        return max_len