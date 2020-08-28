 


def peaks(A):
    
    peak = 0 
    for element in A:
        if element > peak:
            peak = element


    return A.index(peak)