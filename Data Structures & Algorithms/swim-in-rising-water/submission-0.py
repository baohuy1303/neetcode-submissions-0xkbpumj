import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # bfs + min heap to know whats the minmal max path or water level
        # we should go to next by spreading ourselves

        visited = set((0,0))
        q = [(grid[0][0],0,0)]
        heapq.heapify(q)
        n = len(grid)
        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q:
            level, i, j = heapq.heappop(q)

            for dr, dc in dir:
                nr = i + dr
                nc = j + dc
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                    if nr == n-1 and nc == n-1:
                        return max(level, grid[nr][nc])

                    visited.add((nr, nc))
                    heapq.heappush(q, (max(level, grid[nr][nc]), nr, nc ))

