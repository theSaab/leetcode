


def divide( nums, k ):

    nums.sort()
    if len(nums) % k != 0:
        return False
    print(nums)
    for i,num in enumerate(nums):
        print(num)
        try:
            if nums[i+1] != num and nums[i+1] != num + 1:
                return False
        except:
            return True
    
print(divide([3,2,1,2,3,4,3,4,5,9,10,11], 3))