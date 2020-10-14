

def odds( arr ):

    for i,num in enumerate(arr):
            try:
                if num % 2 != 0:
                    if arr[i+1] % 2 != 0 and arr[i+2] % 2 != 0:
                        return True
            except:
                break
    else:
        return False

