


def unique( arr ):

    nums = []
    spare = []

    for element in arr:
        # print(arr)
        # print(spare)
        # print(element)
        if element not in spare:
            spare.append(element)
            if arr.count(element) not in nums:
                nums.append(arr.count(element))
            else:
                return False
        
    return True

print(unique([1,2]))