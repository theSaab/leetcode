

def ranking( arr ):
    copy = arr
    print(arr)
    print(copy)
    copy.sort()
    print()
    print(arr)
    print(copy)
    for i,element in enumerate(arr):
            arr[i] = copy.index(element)+1
    print(copy)

    return arr

print(ranking([4,1,2,3]))