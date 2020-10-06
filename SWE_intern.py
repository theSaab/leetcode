
# Given an array of 0's and 1's, move all of the 0's to the beginning of the array and all of the 1's to the end of the array.
def move0( arr ):
    j = 0
    i = 0
    while j < len(arr):
        
        if arr[i] == 1:
            # print('here')
            del arr[i]
            i -= 1
            arr.append(1)
        j += 1
        i += 1
    return arr
