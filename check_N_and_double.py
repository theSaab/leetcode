


def check( arr ):

    for i,num in enumerate(arr):
        for elem in arr[i+1:]:
            if elem * 2  == num:
                return True
            elif elem == num * 2:
                return True
    else:
        return False