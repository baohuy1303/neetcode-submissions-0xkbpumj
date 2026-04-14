class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # arr stores 3 arr, each arr has 3 set of 3x3 boards
        # arr stores 9 set of col
        # check horizontal/row while traversing

        col_set = [set() for _ in range(9)]
        print(col_set)
        board_set = [[set() for _ in range(3)] for _ in range(3)]
        ''' board_dict = {
            0: 0,
            1: 0,
            2: 0,
            3: 1,
            4: 1,
            5: 1,
            6: 2,
            7: 2,
            8: 2
        } '''

        for i in range(9):
            row_set = set()
            for j in range(9):
                cur_num = board[i][j]
                if cur_num == ".":
                    continue
                if cur_num in row_set or cur_num in col_set[j]:
                    return False
                cur_row_num = i // 3 #board_dict[i]
                cur_col_num = j // 3 #board_dict[j]
                cur_board_set = board_set[cur_row_num][cur_col_num]

                if cur_num in cur_board_set:
                    return False
                cur_board_set.add(cur_num)
                row_set.add(cur_num)
                col_set[j].add(cur_num)

        return True