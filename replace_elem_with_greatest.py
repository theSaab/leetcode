




def replaceElement(arr):

    for i,element in enumerate(arr[:-1]):
        highest = 0
        try:
            for num in arr[i+1:]:
                if num >= highest:
                    highest = num
            arr[i] = highest
        except:
            continue
    arr[-1] = -1
    return arr