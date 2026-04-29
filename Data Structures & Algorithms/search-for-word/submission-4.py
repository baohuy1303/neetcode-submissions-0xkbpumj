class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        '''
        go until find starting char
        then explore in 4 dir 
        compare path_str to word[:len(path_str)]. If they're the same continue explore
        else return.

        base: if path_str == word: return True
        mark visited #
        '''
        # up, down, left, right
        res = False
        dir = [(-1,0), (1,0), (0, -1), (0, 1)]
        def dfs(i, j, k):
            if k >= len(word):
                return True

            for coord in dir:
                new_i = i + coord[0]
                new_j = j + coord[1]            
                if 0 <= new_i <= len(board) - 1 and 0 <= new_j <= len(board[i]) - 1:

                    cur_char = board[new_i][new_j]

                    if cur_char == "#":
                        continue
                    if cur_char == word[k]:
                        board[new_i][new_j] = "#"
                        if dfs(new_i, new_j, k+1) == True:
                            return True
                        board[new_i][new_j] = cur_char
                else:
                    continue
            return False

        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                if word[0] == board[i][j]:
                    temp = board[i][j]
                    board[i][j] = "#"
                    if dfs(i, j, 1) == True:
                        return True
                    board[i][j] = temp
        return False

