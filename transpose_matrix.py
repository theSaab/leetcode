

def transpose(matrix):
    
    ret_mat = []
    index = 0
    inner = []
    for i in range(len(matrix[0])):
        for element in matrix:
            inner.append(element[index])
            
        ret_mat.append(inner)
        inner = []
        index += 1

    return ret_mat

print(transpose([[1,2,3],[4,5,6],[7,8,9]]))