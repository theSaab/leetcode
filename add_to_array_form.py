

def add(A, K):

    num = ''
    for element in A:
        num += element
    
    arr = []

    new = int(num) + K

    for char in str(new):
        arr.append(char)
    
    return arr