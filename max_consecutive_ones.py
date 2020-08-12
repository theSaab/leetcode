

def ones(nums):

    count = 0
    new_count = 0
    for element in nums:
        if element == 1:
            new_count += 1
        else:
            if new_count >= count:
                count = new_count
                new_count = 0
    else:
        if new_count >= count:
            count = new_count
            new_count = 0

    print(count)


ones([1, 1, 1, 1, 1, 1, 0, 0,1,1,1,1,1,1,1,1,1, 0, 1, 1, 1, 1, 1, 1, 1, 1])
