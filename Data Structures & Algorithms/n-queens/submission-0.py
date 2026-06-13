''' placing n queens on an n x n chessboard

NO QUEENS can attack eachother:
    in each queens path: horizontally, vertically, and diagonally - theres no other queen

return a list of board layouts - list(list(str))

1 <= n <= 8

how do we know where to place a queen:
    - to place or not place
        + if want to place, check all 8 dirs to see if theres another queen?
        + if can place, place. else go to next coord
        + if placed, add all 8 dirs into a set? so other queens can avoid

how do we guarantee n queens on the board:
    - we can try to place/dfs at each coord. if we finish the board (bottom-right) and theres n queens -> valid
    else we try the next coord at the top-level
    
    - we need to place n queens, so there must be 1 queen per row (n*n board):
        + row by row? first row''s will cascade downwards, and limits the options of placing for later ones
        + for each queen we place, if going down that path doesnt work, we''ll try another 1 if theres a free
        coord on the same row

how do we mark coord as not able to place queens:
    - create a board 0s and 1s, and whenever a queen is placed mark as 1. but this means for each queen
    we want to place we need to check all 8 dirs to see if it collides with anything.
    what if when we place a queen, we flip the 0s to 2s in 8 dirs starting from the 1 (queen)?
        - but that means when we backtrack, its hard to revert those 2s.
    - hash set seen? when placing 1 it locks the entire row and col so we can just log that
    but what about diagonals?
        - positive diagonals have same sum (3,0) (2,1) (1,2) (0,3)
        - negative diagonals have same diff (0,0) (1,1) (2,2) (3,3) | (0,1) (1,2) (2,3)...

mock:
create empty list(list(str)) that represents n*n board

try out all cols in 1st row, mark the row and column and pos_diag and neg_diag
move to new row, and try each 1 until found a valid coord to place
then repeat

... until the end. we check. if not enough, backtrack
-> remove locked coord.

try out all cols in i row, mark to seen, then modify board, dfs(i+1, seen.copy()) if found valid
then seen.remove(...) and remove Q from board. and continue the loop until the end of loop where we just return

maintain row, col, seen

if succesful (i==n) (because theres only 1 queen per row) then we append to res
convert the board to flat string
 '''

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for _ in range(n)]

        def dfs(i, seen, pos_diag, neg_diag):
            if i == (n):
                final = []
                for row in range(n):
                    final.append("".join(board[row]))
                res.append(final)
            
            for j in range(n):
                if j in seen or i+j in pos_diag or i-j in neg_diag:
                    continue
                seen.add(j)
                pos_diag.add(i+j)
                neg_diag.add(i-j)
                board[i][j] = "Q"
                dfs(i+1, seen, pos_diag, neg_diag)
                seen.remove(j)
                pos_diag.remove(i+j)
                neg_diag.remove(i-j)
                board[i][j] = "."
                
            return
        
        dfs(0, set(), set(), set())
        return res










