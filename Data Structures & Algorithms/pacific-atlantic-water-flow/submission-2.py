class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # go reverse, go from border and get to the origin
        # if we can reach a cell from the border, then it belongs to that ocean hashset
        # at then end we go thru all cells and see if any cell are in both sets
        # in both sets mean from that origin we can reach both oceans

        pacific = set()
        atlantic = set()
        rows = len(heights)
        cols = len(heights[0])

        dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        def dfs(i, j, hash_set):
            hash_set.add((i, j))
            for x, y in dir:
                new_row = i + x
                new_col = j + y

                if 0 <= new_row < rows and 0 <= new_col < cols:
                    if heights[new_row][new_col] >= heights[i][j] and (new_row, new_col) not in hash_set:
                        dfs(new_row, new_col, hash_set)
            return
        
        for c in range(cols):
            dfs(0, c, pacific)
            dfs(rows - 1, c, atlantic)
        
        for r in range(rows):
            dfs(r, 0, pacific)
            dfs(r, cols - 1, atlantic)
            
        res = []
        for i in range(rows):
            for j in range(cols):
                if (i, j) in pacific and (i, j) in atlantic:
                    res.append([i, j])
        
        return res

