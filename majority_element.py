
'''
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
'''


list = [2, 2, 1, 1, 1, 2, 2]


def majority(input):

    arr = {}
    for element in input:
        if element in arr:
            arr[element] += 1
            continue
        else:
            arr[element] = 1
    else:
        max = 0
        for element in arr:
            if arr[element] > max:
                max = arr[element]
                key = element
        else:
            return(key)


majority(list)
