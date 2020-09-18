


def dups(arr):

    save = len(arr)
    i = 0
    space = True
    while space:
        try:
            if arr[i] == 0:
                try:
                    arr.insert(i+1, 0)
                    i += 1
                except:
                    space = False
                    continue  
        except:
            arr = arr[0:save]
            break
        i += 1  
    
    
    return arr
print(dups([1,0,2,3,0,4,5,0]))