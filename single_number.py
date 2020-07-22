
'''
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
'''


list = [2, 2, 1, 1, 1, 2, 2]


def single(input):

    arr = {}
    for element in input:
        if element in arr:
            arr[element] += 1
            continue
        else:
            arr[element] = 1
    else:
        for element in arr:
            if arr[element] == 1:
                print(element)
                break

single([4,1,2,1,2])
