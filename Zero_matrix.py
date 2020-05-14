


matrix = [[1, 0, 1],
          [4, 0, 6],
          [7, 1, 9],
          [0, 3, 1],
          [0, 3, 1],
          [0, 3, 1],
          [0, 3, 1],
          [0, 3, 1]]

ret_matrix =[[1, 0, 1],
          [4, 0, 6],
          [7, 1, 9],
          [0, 3, 1],
          [0, 3, 1],
          [0, 3, 1],
          [0, 3, 1],
          [0, 3, 1]]

zero_in = 0
out_count = 0
blank = lambda: [0] * len(matrix[0])

for row in matrix:
    col = 0
    for num in row:
        if num == 0:
            for ret_row in ret_matrix:
                ret_row[col] = 0
        else:
            col += 1
                      
    if 0 in row:
        ret_matrix[out_count] = blank()
    out_count += 1
    
print('\n')  
for row in ret_matrix:
    print(row)

    