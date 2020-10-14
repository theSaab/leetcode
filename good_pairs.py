

def pairs( nums ):
    
    count = 0
    for i,num in enumerate(nums):
        for elem in nums[i+1:]:
            if elem == num:
                count += 1

    return count