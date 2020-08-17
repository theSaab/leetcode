

def array(nums):

    count = 0 
    begining = nums[0]
    nums = nums[1:]
    i = 0
    while count < 2:
        if i == len(nums):
            for i,num in enumerate(nums):
                if num < begining:
                    print(str(num) + ' count')
                    count += 1
                    begining = nums[i+1]
                    nums = nums[i+2:]
                    break
        else:
            break

    if count != 1:
        return True
    else:
        return False 
  
print(array([4,2,1]))