

sudoku = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]

other = [["8", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

new = [[".", ".", ".", ".", "5", ".", ".", "1", "."],
       [".", "4", ".", "3", ".", ".", ".", ".", "."],
       [".", ".", ".", ".", ".", "3", ".", ".", "1"],
       ["8", ".", ".", ".", ".", ".", ".", "2", "."],
       [".", ".", "2", ".", "7", ".", ".", ".", "."],
       [".", "1", "5", ".", ".", ".", ".", ".", "."],
       [".", ".", ".", ".", ".", "2", ".", ".", "."],
       [".", "2", ".", "9", ".", ".", ".", ".", "."],
       [".", ".", "4", ".", ".", ".", ".", ".", "."]]


def valid_sudoku(board):
    line_count = 0
    for element in board:
        line = element
        count = 0
        for element in line:
            single_num = element
            if single_num == '.':
                count += 1
                continue
            else:

                if single_num in line[count + 1:]:
                    return False
                    break
                else:
                    for element in board[line_count + 1:]:
                        if element[count] == single_num:
                            return False
                            break
                        else:
            count += 1
        line_count += 1

    else:
        return True


print(valid_sudoku(new))
