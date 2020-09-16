

def trade(A, B):

    len_a = 0
    len_b = 0
    
    for element in A:
        len_a += element
    
    for element in B:
        len_b += element
    
    trade_arr = []
    for i,numA in enumerate(A):
        for numB in B:
            if len_a - numA + numB == len_b - numB + numA:
                 trade_arr.append(numB)
                 trade_arr.append(numA)
