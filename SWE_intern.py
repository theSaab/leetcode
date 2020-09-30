

def remove(arr, k):

    index_count = 0
    count = 0
    while len(arr) > 1:
        
        count += 1
        if count == k:
            arr.pop(index_count%len(arr))
            count = 1
        index_count += 1
        print(arr)
    return arr


print(remove([1,2,3,4,5,6,7], 4))