

def mismatch(list):

    
    list.sort()

    for i in range(1, len(list) + 1):
        if i not in list:
            missing = i
        elif list.count(i) > 1:
            extra = i

    return [extra, missing] 


print(mismatch([1, 2, 2, 4]))
