from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # bfs, scan grid and append queue of rotten fruits. each level counts as +1 min
        # pop each rotten, and check 4 dir to append fresh fruits in (those fruits are now rotten)
        # mark fresh -> rotten (change 1 to 2)
        # return -1 if first scan has no rotten, or at the end scan still has fresh

        q = deque()
        rows = len(grid)
        cols = len(grid[0])
        num_of_fresh = 0

        for i in range(0, rows):
            for j in range(0, cols):
                cur = grid[i][j]
                if cur == 1:
                    num_of_fresh += 1

                if cur == 2:
                    q.append([i,j])

        if len(q) == 0 and num_of_fresh > 0:
            return -1
        
        dir = [[-1, 0], [1,0], [0,-1], [0,1]]
        time = 0
        
        while q:
            print(q)
            level_size = len(q)
            
            for _ in range(level_size):
                rotten = q.popleft()
                for x, y in dir:
                    new_row = rotten[0] + x
                    new_col = rotten[1] + y

                    if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == 1:
                        q.append([new_row, new_col])
                        grid[new_row][new_col] = 2
                        num_of_fresh -= 1
            
            if q:
                time += 1

        if num_of_fresh == 0:
            return time
        return -1


