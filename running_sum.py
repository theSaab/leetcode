

def sum( nums ):
    arr = []
    count = 0
    for element in nums:
        count += element
        arr.append(count)

    return arr