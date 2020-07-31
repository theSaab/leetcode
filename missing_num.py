


def missing(list):

    total = len(list)
   
    else:
            
        for i in range(total + 1):
            if i not in list:
                return i
        
print(missing([9,6,4,2,3,5,7,0,1]))