



def special_int( arr ):

    dik = {}
    for num in arr:
        if num not in dik:
            dik[num] = 1
        else:
            dik[num] += 1
    
    big = 0

    for node in dik:
        print(node)
        print(dik[node]/len(arr))
        if (dik[node]/len(arr) >= 0.25) or (dik[node]/len(arr) >= big):
            print(dik[node]/len(arr))
            big = node

    return big

print(special_int([1,2,3,3]))