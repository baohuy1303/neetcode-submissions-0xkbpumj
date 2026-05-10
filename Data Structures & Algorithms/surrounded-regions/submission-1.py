class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # travel the edge and go from any O at the edge
        # add each cell from O edge to a list

        keep = set()
        rows = len(board)
        cols = len(board[0])

        dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        def dfs(i, j):
            for dr, dc in dir:
                nr = i + dr
                nc = j + dc

                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in keep:
                    if board[nr][nc] == "O":
                        keep.add((nr, nc))
                        dfs(nr, nc)
            return
            
        for i in range(0, rows):
            for j in range(0, cols):
                if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
                    if board[i][j] == "O":
                        keep.add((i, j))
                        dfs(i, j)

        for i in range(0, rows):
            for j in range(0, cols):
                if board[i][j] == "O" and (i, j) not in keep:
                    board[i][j] = "X"
            
