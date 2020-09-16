

def mono(A):
  
    type = 3
    for i,element in enumerate(A):
        if type == 0:
            try:
                if element < A[i+1]:
                    return False
            except:
                return True
        elif type == 1:
            try:
                if element > A[i+1]:
                    return False
            except:
                return True
        else:
            try:
                if element > A[i+1]:
                    type = 0
                elif element < A[i+1]:
                    type = 1
            except:
                continue
    else:
        return True
            
            
