

def lucky(arr):
    
    count = -1
    for element in arr:
        if arr.count(element) == element and arr.count(element) > count:
            count = arr.count(element)
    
    return count