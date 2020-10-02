


def counter( nums ):
    
    arr = []
    for i,num in enumerate(nums):
        count = 0
        for j,elem in enumerate(nums):
            if j != i:
                if elem < num:
                    count += 1
        arr.append(count)

    return arr