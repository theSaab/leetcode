

'''
    given a NxN matrix, rotate the numbers by 90 degrees
    difficult
'''
# input matrix
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

# assigning variables 
len_matrix = len(matrix)
cols = 0
ret_matrix = []

# creating the blank matrix
for i in range(len_matrix):
    ret_matrix.append([])

# appending numbers to blank matrix
for i in range(len_matrix):
    rows = len(matrix) - 1

    # iterates through the given column of each nested list
    while rows >= 0:
        
        # appending number
        ret_matrix[i].append(matrix[rows][cols])
        rows -= 1
    # change the column
    cols += 1

print(ret_matrix)
