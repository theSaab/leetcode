
from delete_middle_node import LinkedLists


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
                
                if single_num in line[count + 1 :]:
                    print('Here.')
                    break
                else:
                    for element in board[line_count + 1 :]:
                        if element[count] == single_num:
                            print('Not Valid.')
                            break
                count += 1
        line_count += 1

        
    else:
        print('Valid')


valid_sudoku(sudoku)
