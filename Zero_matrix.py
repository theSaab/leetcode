

import time
x = time.time()
print(x)

matrix = [[4, 0, 6],
          [7, 1, 9],
          [5, 5, 0]]

ret_matrix = [[4, 0, 6],
              [7, 1, 9],
              [5, 5, 0]]

zero_in = 0
out_count = 0


def blank():
    return [0] * len(matrix[0])


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

for element in ret_matrix:
    print(element)