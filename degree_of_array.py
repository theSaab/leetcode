

def degree(nums):
    
    first = int(nums.index(nums[0]))
    last = int((len(nums) -1) - list(reversed(nums)).index(nums[0]))
    count = nums.count(nums[0])     
    degree = last - first
    arr = [nums[0]]

    for element in nums[1:]:

        if element not in arr:
            arr.append(element)    
            first = int(nums.index(element))
            last = int((len(nums) -1) - list(reversed(nums)).index(element))
            
            if nums.count(element) >= count:
                if last - first + 1 <  degree:
                    count = nums.count(element)
                    degree = last - first + 1
                    # print(count)
                    # print(degree)
            # elif nums.count(element) >= count and last - first + 1 <  degree:
            #     count = nums.count(element)    
            #     degree = last - first + 1
            #     print(count)
            #     print(degree)

        return degree

print(degree([1,2,2,3,1]))